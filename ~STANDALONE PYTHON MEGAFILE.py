#-------- EXPERIMENT SEPARATOR I --------#
#---- PROGRAM SEPARATOR ----#
X = 10
Y = 20
print("X + Y =", X + Y)
print("X - Y =", X - Y)
print("X * Y =", X * Y)
print("X / Y =", X / Y)
print("X % Y =", X % Y)
print("X // Y =", X // Y)
print("X ** Y =", X ** Y)

#---- PROGRAM SEPARATOR ----#
x = 20
y = 25
print('x == y is', x == y)
print('x != y is', x != y)
print('x > y is', x > y)
print('x < y is', x > y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

#---- PROGRAM SEPARATOR ----#
x = 10
y = 20
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)

#---- PROGRAM SEPARATOR ----#
a = 10
b = 4
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)

#---- PROGRAM SEPARATOR ----#
a = 10
b = 7
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if a in list1:
	print("a is present in list1")
else:
	print("a is absent in list1")
if b in list1:
	print("b is present in list1")
x = 23
y = 20
list2 = [10, 15, 20, 30, 35, 40, 45, 50]
if x not in list2:
	print("x is unavailable in list2")
else:
	print("x is available in list2")
if y not in list2:
	print("y is unavailable in list2")
else:
	print("y is available in list2")

#---- PROGRAM SEPARATOR ----#
x = 6
if type(x) is not int:
	print("true")
else:
	print("false")

#------ QUESTION AREA SEPARATOR ------#
#---- PROGRAM SEPARATOR ----#
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

#---- PROGRAM SEPARATOR ----#
x = 10 + 5 * 2
y = (10 + 5) * 2
z = 10 + 5 * 2 ** 2
print(x)
print(y)
print(z)

#-------- EXPERIMENT SEPARATOR II --------#
#---- PROGRAM SEPARATOR ----#
numbers = [1, 2, 3, 4, 5]
for num in numbers:
	print(num)

#---- PROGRAM SEPARATOR ----#
arr = [10, 20, 30, 40, 50]
total = 0
for val in arr:
	total += val
print("Sum =", total)

#---- PROGRAM SEPARATOR ----#
arr = [12, 45, 23, 51, 19, 8]
max_val = arr[0]
for num in arr:
	if num > max_val:
		max_val = num
print("Maximum Element:", max_val)

#---- PROGRAM SEPARATOR ----#
student = {"name": "Mrunal", "age": 21, "marks": 92}
for key, value in student.items():
	print(key, ":", value)

#---- PROGRAM SEPARATOR ----#
string = "Python"
reversed_str = ""
for ch in string:
	reversed_str = ch + reversed_str
print("Reversed:", reversed_str)

#---- PROGRAM SEPARATOR ----#
arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for num in arr:
	freq[num] = freq.get(num, 0) + 1
print(freq)

#---- PROGRAM SEPARATOR ----#
arr = [4, 7, 1, 9, 3]
key = 9
found = False
for val in arr:
	if val == key:
		found = True
		break
print("Element Found!" if found else "Not Found")

#---- PROGRAM SEPARATOR ----#
n = 5
fact = 1
for i in range(1, n+1):
	fact *= i
print("Factorial of", n, "is", fact)

#---- PROGRAM SEPARATOR ----#
n = 10
a, b = 0, 1
for _ in range(n):
	print(a, end=" ")
a, b = b, a + b

#---- PROGRAM SEPARATOR ----#
num = -5
if num >= 0:
	print("Positive")
else:
	print("Negative")

#---- PROGRAM SEPARATOR ----#
marks = 85
if marks >= 90:
	print("Grade: A+")
elif marks >= 75:
	print("Grade: A")
elif marks >= 60:
	print("Grade: B")
else:
	print("Grade: C")

#---- PROGRAM SEPARATOR ----#
num = 15
if num > 0:
	if num % 2 == 0:
		print("Positive even number")
	else:
		print("Positive odd number")
else:
	print("Number is zero or negative")

#---- PROGRAM SEPARATOR ----#
a, b, c = 10, 25, 15
if a > b:
	if a > c:
		print("Largest:", a)
	else:
		print("Largest:", c)
else:
	if b > c:
		print("Largest:", b)
	else:
		print("Largest:", c)

#---- PROGRAM SEPARATOR ----#
num = 30
if num % 2 == 0:
	if num % 5 == 0:
		print("Even and divisible by 5")
	else:
		print("Even but not divisible by 5")
else:
	print("Odd number")

#---- PROGRAM SEPARATOR ----#
arr = [3, 8, 1, 9, 5]
key = 9
found = False
for val in arr:
	if val == key:
		found = True
		break
if found:
	print("Element Found")
else:
	print("Element Not Found")

#---- PROGRAM SEPARATOR ----#
for i in range(1, 4):
	for j in range(1, 4):
		print(j, end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
for i  in range(1, 6):
	for j in range(1, i + 1):
		print("*", end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
for i in range (5, 0, -1):
	for j in range(1, i + 1):
		print("*", end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
for i in range (5, 0, -1):
	for j in range(1, i + 1):
		print(j, end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
rows = 5
for i in range(1, rows + 1):
	print(" " * (rows - i), end="")
	print("* " * i)

#---- PROGRAM SEPARATOR ----#
ch = 65
for i in range(5):
	for j in range(i + 1):
		print(chr(ch), end=" ")
	ch += 1
	print()

#---- PROGRAM SEPARATOR ----#
num = 1
for i in range(1, 6):
	for j in range(1, i + 1):
		print(num, end=" ")
		num += 1
	print()

#---- PROGRAM SEPARATOR ----#
rows = 5
for i in range(1, rows + 1):
	print(" " * (rows - i) + "*" * i)
for i in range(rows - 1, 0, rows + 1):
	print(" " * (rows - i) + "*" * i)

#---- PROGRAM SEPARATOR ----#
for num in range(1, 11):
	if num % 3 == 0:
		continue
	print(num)

#---- PROGRAM SEPARATOR ----#
for letter in "PYTHON":
	if letter == "H":
		pass
		print("Pass executed for:", letter)
	print("Current:", letter)

#------ QUESTION AREA SEPARATOR ------#
#---- PROGRAM SEPARATOR ----#
n = 5
if (n > 5):
	print("*")
elif n == 5:
	print("**")
else:
	print("***")

#---- PROGRAM SEPARATOR ----#
n = int(input("Enter n: "))
if n % 2 == 0:
	print("Even")
else:
	print("Odd")

#---- PROGRAM SEPARATOR ----#
grade = float(input("Enter grade: "))
if grade >= 95:
	print("S")
elif grade >= 90:
	print("A")
elif grade >= 80:
	print("B")
else:
	print("Below B")

#---- PROGRAM SEPARATOR ----#
a = [8, 2, 4, 1, 3]
key = 1
i = 0
while key != a[i]:
	print(a[i])
	i += 1

#---- PROGRAM SEPARATOR ----#
a = [8, 2, 4, 1, 3]
key = 10
i = 0
found = 0
while i < len(a):
	if key == a[i]:
		print("Found")
		found = 1
	i += 1
if not found:
	print("Not Found")

#---- PROGRAM SEPARATOR ----#
n = int(input("Enter n: "))
sum = 0
while n != 0:
	sum += n % 10
	n //= 10
print("Sum is", sum)

#---- PROGRAM SEPARATOR ----#
for i in range(1, 3+1):
	for j in range(1, i+1):
		print("*", end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
for i in range(1, 10 + 1):
	if i % 4 == 0:
		continue
	print(i, end=" ")

#---- PROGRAM SEPARATOR ----#
n = 4
if n == 4:
	pass
else:
	print("Dummy Output")

#---- PROGRAM SEPARATOR ----#
for i in range(1, 20 + 1):
	if i % 6 == 0:
		print(f"{i} is divisible by 6 & hence 3")
		continue
	if i % 3 == 0:
		print(f"{i} is divisible by 3")
	if i % 15 == 0:
		print(f"{i} is divisible by 15, breaking loop")
		break

#---- PROGRAM SEPARATOR ----#
for i in range(1, 10 + 1):
	if i % 2 == 0:
		continue
	if i % 3 == 0:
		pass
	if i % 8 == 0:
		break
	else:
		print(i, end=" ")
print("\nOut of Loop")

#---- PROGRAM SEPARATOR ----#
n = int(input("Enter n: "))
if n > 0:
	print("+ve")
elif n == 0:
	print("Zero")
else:
	print("-ve")

#---- PROGRAM SEPARATOR ----#
for i in range(2, 50):
	if (i % 2) == 0:
		print(i, end=" ")

#---- PROGRAM SEPARATOR ----#
n = int(input("Enter n: "))
fac = 1
while n > 1:
	fac *= n
	n -=1
print("Factorial is", fac)

#---- PROGRAM SEPARATOR ----#
for i in range(1, 3 + 1):
	for j in range(1, i + 1):
		print("*", end=" ")
	print()

#---- PROGRAM SEPARATOR ----#
yr = int(input("Enter year:" ))
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
	print("Leap Year")
else:
	print("Not Leap Year")

#-------- EXPERIMENT SEPARATOR III --------#
#----PROGRAM SEPARATOR ----#
a = [1, 'hello', 3.14, True]
print(a)
print(a[1])

#---- PROGRAM SEPARATOR ----#
a = list((1, 2, 3, 'apple', 4.5))
b = list("MIT")
print(a)
print(b)
c = [2] * 5
print(a)

#---- PROGRAM SEPARATOR ----#
a = []
a.append(10)
print("append(10):", a)
a.insert(0, 5)
print("insert(0, 5):", a)
a.extend([15, 20, 25])
print("extend([15, 20, 25]):", a)
a.clear()
print("clear()", a)

#---- PROGRAM SEPARATOR ----#
my_list = [{'name': 'Alice', 'age': 30},
{'name': 'Bob', 'age': 25}]
new_dict = {'name': 'Charlie', 'age': 40}
my_list.append(new_dict)
print(my_list)

#---- PROGRAM SEPARATOR ----#
list1 = [ 1, 2, 3, 4, 5, 6 ]
num_tuple = (4, 5, 6)
list1.insert(2, num_tuple)
print(list)
print(list1[2][1]) # => 5

#---- PROGRAM SEPARATOR ----#
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][0])

#---- PROGRAM SEPARATOR ----#
squares = [x ** 2 for x in range(1, 6)]
print(squares)

#---- PROGRAM SEPARATOR ----#
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::])
print(a[:])
print(a[3:8])
print(a[1::3])
print(a[1:5:2])
print(a[-1])
print(a[-4])
print(a[-4:-1])
print(a[::-1])

#---- PROGRAM SEPARATOR ----#
my_list = ['apple', 'banana', 'cherry']
a, b, c = my_list
print(a)
print(b)
print(c)

#---- PROGRAM SEPARATOR ----#
t1 = (1, 2, 3, 4,5,6,7)
a, b, *c = t1
print(f"Original tuple: {t1}")
print(f"Unpacked variables: a={a}, b={b}, c={c}")

#------ QUESTION AREA SEPARATOR ------#
#---- PROGRAM SEPARATOR ----#
l1 = list(i + 1 for i in range(1, 4))
l2 = [1] * 5

#---- PROGRAM SEPARATOR ----#
l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2
print(l3)
l4 = [1] * 4
print(l4)
l5 = [8, 2, 4, 1, 3]
if 1 in l5:
	print("1 is present in l5")
else:
	print("1 is absent in l5")

#---- PROGRAM SEPARATOR ----#
matrix = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
print(len(matrix[0]))
print(len(matrix[1]))
print(len(matrix[2]))
m2 = [[1, 2], [3, 4, [5, 6, 7]]]
print(len(m2[1][2]))

#---- PROGRAM SEPARATOR ----#
l1 = [1, 2, 3, 4]
l1.append(4.5)
l1.remove(1)
print(l1)

#---- PROGRAM SEPARATOR ----#
a = [1, 2, 3, 4, 5]
print(a[1::2])
print(a[1:4])
print(a[:4:2])
print(a[::2])
print(a[::4])
print(a[::])

#---- PROGRAM SEPARATOR ----#
a = [0, 1, 2, 3, 4]
a.append(5)
a.insert(3, 2.5)
a.remove(3)
a.extend((5.5, 6))
print(a)
a.clear()
print(a)

#---- PROGRAM SEPARATOR ----#
a = [8, 2, 4, 1, 3]
b = sorted(a)
print(b)
a.sort()
print(a)

#---- PROGRAM SEPARATOR ----#
a = [8, 2, 4, 1, 3, True]
print(max(a))
print(min(a))
print(sum(a))
print(len(a))

#---- PROGRAM SEPARATOR ----#
a = [8, 2, 4, 1, 3]
a.append(7)
a.insert(3, 8)
a.remove(8)
a.pop()
a.extend((9, 5))

#---- PROGRAM SEPARATOR ----#
a = b = [0, 1, 2]
a.append((3, 4))
a.append(5, 6)
print(a)

#---- PROGRAM SEPARATOR ----#
a = [0, 1, 2, 3, 2]
print(a.count(2))
print(a.index(3))
a.clear()
print(a)

#---- PROGRAM SEPARATOR ----#
a = [1, 2, 3]
b = a
c = a.copy()
a.clear()
print(b)
print(c)

#-------- EXPERIMENT SEPARATOR IV --------#
#---- PROGRAM SEPARATOR ----#
numers = (1, 2, 3)
print(numbers)

#---- PROGRAM SEPARATOR ----#
a = (1)
b = (1, )
print(a)
print(b)

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3, 4)
l = list(t)
l.append(5)
print("Modified List:", l)
t = tuple(l)
print("List->Tuple:", t)

#---- PROGRAM SEPARATOR ----#
n = (15, 3, 8, 22, 5, 13)

max = min = n[0]
for n in n:
	if n > max:
		max = n
	elif n < min:
		min = n
print("Max:", max)
print("Min:", min)

#---- PROGRAM SEPARATOR ----#
p = [("a", 10), ("b", 20), ("c", 30)]
d = dict(p)
print("Dictionary:", d)

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3, 2, 4, 1, 2)
freq = {}
for item in t:
	freq[item] = freq.get(item, 0) + 1
print("Frequency: ", freq)

#---- PROGRAM SEPARATOR ----#
sq = tuple(x ** 2 for x in range(1, 4))
print("Squared Tuple:", sq)

#---- PROGRAM SEPARATOR ----#
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print("Concatenated Tuple:", combined)
repeated = t1 * 2
print("Repeated Tuple:", repeated)
print("Is 2 in t1?", 2 in t1)
print("Is 10 not in t1?", 10 not in t1)
print("Length of tuple:", len(t1))
print()
colors = ("red", "green", "blue", "yellow", "purple")
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])
print("Colors[0:3]:", colors[0:3])
print("Colors[2:]:", colors[2:])
print("Colors[:4]:", colors[:4])
print("Colors[-3:]:", colors[-3:])
print()
nums = (15, 8, 22, 5, 13, 30)
print("Tuple:", nums)
print("Length:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))
print("Sorted (as list):", sorted(nums))
print()

#------ QUESTION AREA SEPARATOR ------#
#----PROGRAM SEPARATOR ----#
t = (1, 2, 3, 4)
t2 = (1, )
t3 = 1, 2, 3
l = [1, 2, 3]
t4 = tuple(l)
t5 = tuple(x for x in range(1, 5))

#---- PROGRAM SEPARATOR ----#
nt = (1, (2, 3, 4))
print(nt[1][2])

#---- PROGRAM SEPARATOR ----#
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)
t4 = (4, ) * 3
print(t4)
t5 = (8, 2, 4, 1, 3)
if 4 in t:
	print("4 is present")
else:
	print("4 is absent")

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3)
t.append(4)

#---- PROGRAM SEPARATOR ----#
t = (1, 2, [3, 4])
t[2][0] = "not 3 anymore"
print(t)

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3)
print(t[0])
print(t[-1])
print(t[-2])
print(t[::])
print(t[1:4:2])
print(t[:3])

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3, (4, 5))
print(t[3][0])
print(t[2:4:])

#---- PROGRAM SEPARATOR ----#
t = (1, 2, 3, 4, 5)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))

#---- PROGRAM SEPARATOR ----#
t = (8, 2, 4, 1, 3)
ts = sorted(t)
print(ts)

#---- PROGRAM SEPARATOR ----#
t = (8, 2, 4, 1, 3)
print(max(t))
print(min(t))
print(len(t))
print(sum(t))

#-------- EXPERIMENT SEPARATOR V --------#
#---- PROGRAM SEPARATOR ----#
func = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(func(5))
print(func(-3))
print(func(0))

#---- PROGRAM SEPARATOR ----#
func = [lambda arg = x: arg * 10 for x in range(1, 5)]
for i in func:
	print(i())

#---- PROGRAM SEPARATOR ----#
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

#---- PROGRAM SEPARATOR ----#
s = {1, 2, 3}
s = set([1, 2, 3])
s = set()

#---- PROGRAM SEPARATOR ----#
s = {10, 20, 30}
print(s)
print(type(s))

#---- PROGRAM SEPARATOR ----#
s = set(["a", "b", "c"])
print(s)

#---- PROGRAM SEPARATOR ----#
s = {"Geeks", "for", "Geeks"}
print(s)
s[1] = "Hello" # ERROR LINE
print(s)

#---- PROGRAM SEPARATOR ----#
s = {"a", "b", "c"}
s.add("d")
s.remove("c")
print(s)

#---- PROGRAM SEPARATOR ----#
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(a | b)
print(u)

#---- PROGRAM SEPARATOR ----#
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(a & b)
print(i)

#---- PROGRAM SEPARATOR ----#
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(a - b)
print(d)

#---- PROGRAM SEPARATOR ----#
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)

#---- PROGRAM SEPARATOR ----#
s = {1, 2, 3}
s.clear()
print(s)

#---- PROGRAM SEPARATOR ----#
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))
print(B.issuperset(A))
print(3 in {1, 2, 3})
for item in {1, 2, 3}:
	print(item)
s = {x * x for x in range(5)}
print(s)

#------ QUESTION AREA SEPARATOR ------#
#---- PROGRAM SEPARATOR ----#
