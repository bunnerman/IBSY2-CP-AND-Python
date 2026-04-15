# RUN pip install psutil pygetwindow pywin32 streamlit pandas plotly st-autorefresh FOR DEPENDENCIES
# IF pywin32 ERROR, USE python Scripts/pywin32_postinstall.py -install IN GENERIC CMD PROMPT

import time, json, os, psutil, win32process 
import pygetwindow as gw 
from datetime import datetime, timedelta # deltatime = time since last render

# Config handling
# LOG_DIR = /logs, WEEK_DIR = /weeks, GROUPS_CONFIG = groups.json
LOG_DIR, WEEK_DIR, GROUPS_CONFIG = "logs", "weeks", "groups.json"
for folder in [LOG_DIR, WEEK_DIR]: os.makedirs(folder, exist_ok=True)

# Loads .json file
def load_json(path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            with open(path, "r") as f: return json.load(f)
        except: return {}
    return {}

# Saves temp file, then saves into a proper log file
def atomic_save(path, data):
    temp_path = f"{path}.tmp"
    with open(temp_path, "w") as f: json.dump(data, f, indent=4)
    os.replace(temp_path, path)

# Sees active app window and returns it's process name, eg: windowsterminal.exe
def get_active_app():
    try:
        window = gw.getActiveWindow() # gets active window
        if window:
            _, pid = win32process.GetWindowThreadProcessId(window._hWnd)
            return psutil.Process(pid).name().lower()
    except: return None

def get_custom_date():
    now = datetime.now()
    return (now - timedelta(days=1 if now.hour < 3 else 0)).strftime("%d-%m-%Y")

# Saves log files
def save_tracking_data(exe_name, seconds=5):
    date_str = get_custom_date()
    exe_file = os.path.join(LOG_DIR, f"exe_{date_str}.json")
    
    data = load_json(exe_file)
    data[exe_name] = data.get(exe_name, 0) + seconds
    atomic_save(exe_file, data)

# Handles weekly files, generates at Monday 3AM in /weeks dir.
def generate_weekly_summary():
    now = datetime.now()
    # Check for Monday at 3:00 AM
    if now.weekday() == 0 and now.hour == 3 and now.minute == 0: # 3AM Handling
        start_date = (now - timedelta(days=7))
        end_date = (now - timedelta(days=1))
        summary_path = os.path.join(WEEK_DIR, f"week_{start_date.strftime('%d-%m-%Y')}_to_{end_date.strftime('%d-%m-%Y')}.json")
        
        # Prevents multiple gens within same min
        if os.path.exists(summary_path): return

        weekly_data = {}
        for i in range(1, 8):
            d_str = (now - timedelta(days=i)).strftime("%d-%m-%Y")
            # combines paths into single string for custom naming convention
            day_logs = load_json(os.path.join(LOG_DIR, f"exe_{d_str}.json"))
            for app, sec in day_logs.items():
                weekly_data[app] = weekly_data.get(app, 0) + sec

        atomic_save(summary_path, weekly_data)
        time.sleep(60)
        # Sleep for a minute so no counting in the edge period of 3:00AM to 3:01AM prevents annoying  issues

# Console, default start
print("Tracker active.")
try:
    while True:
        # Generate defualt (weekly) graph
        generate_weekly_summary()
        # Gets active app window (every 5 seconds)
        app = get_active_app()
        if app: 
            save_tracking_data(app)
        # 3. Waits 5 seconds
        time.sleep(5)
except KeyboardInterrupt: 
    print("Stopped.")