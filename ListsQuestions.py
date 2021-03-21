#A4
import random
foodslist = []
for counter in range(0, 5):
  foodslist.append(input())
if 'salt' in foodslist:
  print("Yay! We like the same foods!")
#B1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months.reverse()
print(months)
#B2
i = 0
friends = ['A', 'B', 'C', 'D', 'E']
while friends[i] != 'C':
  i = i+1
print(friends[i], i)
#B3
a = 0
coursecodes = ['ICS2O', 'TEJ3M']
for course in coursecodes:
  if course == 'ICS2O':
    coursecodes[a] = 'ICS3O'
  a += 1
print(coursecodes)
#B4
randoms = []
for counter in range(24):
  randoms.append(random.randint(0,25))
for counter in range(23, 1, -1):
  if randoms[counter] %5 == 0:
    del randoms[counter]
    counter -= 1
print(randoms)
names = ['a', 'b', 'c', 'd', 'e']
a = 0
for name in names:
  print(name)
  print(a)
  a += 1
names = ['a', 'b', 'c', 'd', 'e']
names.pop(3)
print(names)
names = ['a', 'b', 'c', 'c', 'c', 'd', 'c', 'e']
del names[names.index('c')]
print(names)

import random

grades = [90,76, 54, 86 ,71, 99]
print(grades)
for x in grades:
  print(x)

grades.insert(3,20)
print(grades)
names = []
names = ['Jim', 'Sam']
print(names)

names.append('Lisa')
print(names)

names.insert(2, 'Andy')
print(names)


names.remove('Lisa')
print(names)

names.remove('Lisa')
print(names)
del names[1]
print(names)

names.reverse()
print(names)

names.clear()
print(names)

names = ['Jim', 'Sam']
print(listName)
print("Question 1:")
names = []
for counter in range(1,101):
  x = random.uniform(1,100)
  x = round(x, 0)
  names.append(x)
print(names)

print("Question 2:")
sum = 0
for counter in range(0,100):
  sum = sum + names[counter]
sum = sum/100
print(sum)

print("Question 3:")
print(names[0], names[99])

names.clear()
print("Question 4:")
for counter in range(1,11):
  x = round(random.uniform(1,10), 0)
  names.append(x)
print(names)
names.reverse()
print(names)

names.clear()
print("Question 5:")
names = [1, 2, 3, 4, 5]
x = int(input("Gimme a numba"))
print(names[x - 1])

names.clear()
print("Question 6:")
evens = 0
odds = 0
counter = 0
for counter in range(1,11):
  x = random.random() * 10 // 1
  names.append(x)
  if x / 2 == x//2:
    evens = evens + 1
  else:
    odds = odds + 1

print("Evens:", evens, "Odds", odds)
print(names)

print("Question 7:")
names = []
for counter in range(1,11):
  x = random.randint(1,10)
  names.append(x)
min = names[0]
max = names[0]
counter = 0
for counter in range(0,10):
  y = names[counter]
  if min >= y:
    min = y
  else:
    1

for counter in range(0,10):
  y = names[counter]
  if max <= y:
    max = y
  else:
    1
print(names, min, max, sep = '\n')

print("Question 8:")
names = []
for counter in range(0,10):
  x = random.randint(1,10)
  names.append(x)

print(names)
temp = names[7]
names[7] = names[8]
names[8] = temp
print(names)
counter = 0
print("Question 9:")
names = []
for counter in range(0,10):
  x = random.randint(1,10)
  names.append(x)
names.reverse()
z = 0
print("Question C3:")
names = []
for counter in range(0,10):
  x = random.randint(1,10)
  names.append(x)
counter = 0
for counter in range(0,10):
  i = counter
  y = names[counter]
  for z in range(0, counter):
    if y == names[counter]:
      names.remove(names[counter])
    else:
      counter = counter + 1
print(names)

print("A1:")
schedule = ['ENG1D', 'SNC1D', 'MPM1D', 'ICS2O']
print("My schedule:")
for counter in range(1, 5):
  print("Period", counter, ':', schedule[counter-1])
del schedule[3]
schedule.insert(3, 'TEJ3M')
print("My schedule:")
for counter in range(1, 5):
  print("Period", counter, ':', schedule[counter-1])

print("B1:")
max = 0
maxcount = 0
nums = [1, 5, 8, 2, -1]
for counter in range(0, len(nums)):
  if max < nums[counter]:
    max = nums[counter]
    maxcount = counter
print(max, maxcount)

print("B2:")
nums = [1, 2, 2, 3, 3, 3, 4, 5,5,5,7,7]
count = 0
currentNum = -1
for number in nums: #specifying a num
  if number != currentNum:
    currentNum = number
    count += 1
print(count)

print("B3:")
nums = []
n = int(input())
while n != -1:
  nums.append(n)
  n = int(input())
nums.append(0)
for counter in range(0, len(nums), 2):
  a = nums[counter]
  b = nums[counter + 1]
  nums.remove(a)
  nums.remove(b)
  nums.insert(counter+1, a)
  nums.insert(counter, b)
nums.remove(0)
print(nums)

import random

print("A1:")
names = []
n = input()
while n != "quit":
    names.append(n)
    n = input()
print("Length of list:", len(names))
print(names)

print("A2:")
names = []
j = int
for counter in range(0, 5):
    n = input()
    if n == "pizza":
        j = 1
    else:
        counter = counter + 1
if j == 1:
    print("Yay! We like the same foods!")
else:
    print("Too bad, so sad")

print("A3")
print("Enter 5 numbers")
numbers = []
for counter in range(0, 5):
    n = int(input())
    numbers.append(n)
names2 = []
names3 = numbers
a = numbers[0]
names2.append(a)
a = numbers[4]
names2.append(a)
names3.remove(a)
a = numbers[0]

print("Full list:", numbers, "First & Last:", names2, "Removed 1st and Last", names3)

print("B1:")
names = ["Hannah", "Lucas", "", "Katriella"]
for counter in range(0, 3):
    if names[counter] == '':
        a = names[counter]
        names.remove(a)
    else:
        counter = counter + 1
print(names)
print("B2:")
nums = []
for counter in range(0, 25):
    x = round(random.uniform(0, 50), 0)
    nums.append(x)
print(len(nums))
print(nums)
counter = 0
while counter < len(nums):
    if nums[counter] / 5 == nums[counter] // 5:
        a = nums[counter]
        nums.remove(a)
    else:
        counter = counter + 1

print(len(nums))
print(nums)
nums.append(0)
nums2 = []
for counter in range(0, len(nums) + 1):
    a = nums[counter]
    b = nums[counter + 1]
    if b > a:
        nums2.append(b)
    if b == 0:
        break
print(nums2)

sports = ["basketball", "swimming", "running", "baseball", "football", "tennis", "racquetball"]
if len(sports) // 2 == len(sports) / 2:
    a = len(sports)
    b = sports[a // 2]
    c = sports[a // 2 - 1]
    sports.remove(b)
    sports.remove(c)
else:
    a = len(sports)
    b = sports[a // 2]
    sports.remove(b)
print(sports)

print("C1:")
n = int(input("How many numbers of Fibonnaci sequence? "))
Sequence = [1]
a = 1
b = 1
for counter in range(0, n - 1):
    b = a + b
    a = b - a
    Sequence.append(a)
print(Sequence)

b = input().split()
for x in range(0, len(b)):
  b[x] = int(b[x])
x = b[1]
d = []
e = 0
j = 0
c = input().split()
for x in range(0, len(c)):
  c[x] = int(c[x])

for counter in range(0, b[1] - 1):
  for j in range(0, b[0] - 1):
    if e < c[j]:
      e = c[j]
      c.remove(e)
      j = j - 1
    else:
      j = j + 1
  d.append(e)
print(d)
max = 0
g = 0
b = [] # store the maximum number for each line
q = int(input())
for counter in range(1, q):
  a = input().split()
  for x in range(1,2):
    a[x] = int(a[x])
  x = a[0]
  for y in range(a[0], a[1]):
    x = str(x)
    if a[0] < 10:
      a = x[0]
      a = int(a)
      b.append(a)
    elif a[0] < 100:
      a = x[0]
      b = x[1]
      a = int(a)
      b = int(b)
      g = a + b
      b.append(g)
    elif a[0] < 1000:
      a = x[0]
      b = x[1]
      c = x[2]
      a = int(a)
      b = int(b)
      c = int(c)
      g = a + b + c
      b.append(g)
    else:
      a = x[0]
      b = x[1]
      c = x[2]
      d = x[3]
      a = int(a)
      b = int(b)
      c = int(c)
      d = int(d)
      g = a + b + c + d
      b.append(g)
