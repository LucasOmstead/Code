#A4: Check if your favorite food is in a list inputted by the user
import random
foodslist = []
for counter in range(0, 5):
  foodslist.append(input())
if 'salt' in foodslist:
  print("Yay! We like the same foods!")
#B1: Reverse and print the months of the year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months.reverse()
print(months)
#B2: Print the index of a friend without using the index method
i = 0
friends = ['A', 'B', 'C', 'D', 'E']
while friends[i] != 'C':
  i = i+1
print(friends[i], i)
#B3: Change a course code
a = 0
coursecodes = ['ICS2O', 'TEJ3M']
for course in coursecodes:
  if course == 'ICS2O':
    coursecodes[a] = 'ICS3O'
  a += 1
print(coursecodes)
#B4: Make a list of random numbers, then delete any random number divisible by 5
randoms = []
for counter in range(24):
  randoms.append(random.randint(0,25))
for counter in range(23, 1, -1):
  if randoms[counter] %5 == 0:
    del randoms[counter]
    counter -= 1
print(randoms)
#C1: Delete all instances of a certain value in a list
names = ['a', 'b', 'c', 'd', 'e']
a = 0
for name in names:
  print(name)
  print(a)
  a += 1
names = ['a', 'b', 'c', 'd', 'e']
del names[3]
print(names)
names = ['a', 'b', 'c', 'c', 'c', 'd', 'c', 'e']
for counter in range(0, names.count('c')):
  del names[names.index('c')]
print(names)
print(names[0])