# RUN pip install psutil pygetwindow pywin32 streamlit pandas plotly st-autorefresh FOR DEPENDENCIES
# IF pywin32 ERROR, USE python Scripts/pywin32_postinstall.py -install IN GENERIC CMD PROMPT
import streamlit as st
import pandas as pd
import plotly.express as px
import json, os, glob
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Analytics", layout="wide")

# Initialize state
if "dialog_open" not in st.session_state:
    st.session_state.dialog_open = False

# Consistent color mapping for categories
def get_color_map():
    return {
        "Programming/Dev": "hsl(210, 40%, 50%)",
        "Gaming": "hsl(0, 40%, 50%)",
        "Productivity": "hsl(140, 40%, 50%)",
        "Browser": "hsl(280, 40%, 50%)",
        "Chatting": "hsl(30, 40%, 50%)",
        "Other": "hsl(0, 0%, 60%)"
    }

# Data Processing and opening .json
def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, "r") as f: return json.load(f)
        except: return {}
    return {}

def get_groups_from_exes(exe_data):
    groups_config = load_json("groups.json")
    category_totals = {}
    for app_exe, seconds in exe_data.items():
        found = False
        for category, app_list in groups_config.items():
            if app_exe in [a.lower().strip() for a in app_list]:
                category_totals[category] = category_totals.get(category, 0) + seconds
                found = True
                break
        if not found:
            category_totals["Other"] = category_totals.get("Other", 0) + seconds
    return category_totals

# Custom name for exes
def format_name(name):
    aliases = load_json("aliases.json")
    return aliases.get(name, name.lower().replace(".exe", "").capitalize())

def get_current_week_dates():
    now = datetime.now()
    if now.hour < 3: now -= timedelta(days=1)
    monday = now - timedelta(days=now.weekday())
    return [(monday + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(7)]

# Pop-Ups section
@st.dialog("Log Viewer", width="large")
def inspect_file(file_path):
    data = load_json(file_path)
    total_hrs = round(sum(data.values()) / 3600, 1)
    groups_config = load_json("groups.json")
    color_map = get_color_map()
    
    st.write(f"Inspecting: **{os.path.basename(file_path)}**")
    st.subheader(f"Total Usage: {total_hrs}h")
    
    rows = []
    for app, sec in data.items():
        cat_name = "Other"
        for cat, apps in groups_config.items():
            if app in [a.lower().strip() for a in apps]:
                cat_name = cat
                break
        rows.append({"App": format_name(app), "Min": round(sec/60, 2), "Category": cat_name})
    
    df_inspect = pd.DataFrame(rows)
    group_data = get_groups_from_exes(data)
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.write("### Apps (Minutes)")
        fig_a = px.bar(df_inspect.sort_values("Min", ascending=False), 
                       x="Min", y="App", orientation='h',
                       color="Category", color_discrete_map=color_map)
        fig_a.update_traces(hovertemplate="<b>%{y}</b><br>Usage: %{x} Min")
        fig_a.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False)
        st.plotly_chart(fig_a, use_container_width=True)
        
    with col_r:
        st.write("### Categories (Hours)")
        df_p = pd.DataFrame([{"Cat": k, "Hrs": round(v/3600, 2)} for k, v in group_data.items()])
        fig_p = px.pie(df_p, values='Hrs', names='Cat', hole=0.4,
                       color='Cat', color_discrete_map=color_map)
        fig_p.update_traces(hovertemplate="<b>%{label}</b><br>%{value} Hrs<br>%{percent}")
        st.plotly_chart(fig_p, use_container_width=True)

# Sidebar
with st.sidebar:
    if st.toggle("Live Refresh (5s)") and not st.session_state.dialog_open:
        st_autorefresh(interval=5000, key="auto_refresh_main")
            
    all_files = sorted(glob.glob("logs/exe_*.json") + glob.glob("weeks/*.json"), reverse=True)
    selected = st.selectbox("History:", ["None"] + all_files)
    if selected != "None" and st.button("See File"):
        st.session_state.dialog_open = True
        st.rerun() 

# Main/other
current_dates = get_current_week_dates()
st.title(f"Weekly Stats ({current_dates[0]} - {current_dates[-1]})")

# Open Pop-up logic
if st.session_state.dialog_open:
    if selected != "None":
        inspect_file(selected)
    st.session_state.dialog_open = False

weekly_raw = {}
for d in current_dates:
    day_data = load_json(f"logs/exe_{d}.json")
    for app, sec in day_data.items():
        weekly_raw[app] = weekly_raw.get(app, 0) + sec

if weekly_raw:
    total_hrs = round(sum(weekly_raw.values()) / 3600, 1)
    groups_config = load_json("groups.json")
    color_map = get_color_map()

    weekly_rows = []
    for app, sec in weekly_raw.items():
        cat_name = "Other"
        for cat, apps in groups_config.items():
            if app in [a.lower().strip() for a in apps]:
                cat_name = cat
                break
        weekly_rows.append({"App": format_name(app), "Min": round(sec/60, 2), "Category": cat_name})
    
    df_w = pd.DataFrame(weekly_rows)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"App Usage | Total: {total_hrs}h")
        fig_w = px.bar(df_w.sort_values("Min", ascending=False), 
                       x="App", y="Min",
                       color="Category", color_discrete_map=color_map)
        fig_w.update_traces(hovertemplate="<b>%{x}</b><br>Usage: %{y} Min")
        fig_w.update_layout(xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig_w, use_container_width=True)

    with col2:
        st.subheader("Category Used (Hours)")
        weekly_groups = get_groups_from_exes(weekly_raw)
        df_g = pd.DataFrame([{"Cat": k, "Hrs": round(v/3600, 2)} for k, v in weekly_groups.items()])
        fig_g = px.pie(df_g, values='Hrs', names='Cat', hole=0.4,
                       color='Cat', color_discrete_map=color_map)
        fig_g.update_traces(hovertemplate="<b>%{label}</b><br>%{value} Hrs<br>%{percent}")
        st.plotly_chart(fig_g, use_container_width=True)
else:
    st.info("No logs found for this week.")