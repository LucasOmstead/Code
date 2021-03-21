#A1
a1 = int(input())
if a1 > 100:
  print('>100')
else:
  print("<100")
#A2
a2 = int(input())
if a2 / 2 == a2 // 2:
  print("even")
else:
  print("odd")
#A3
a3 = int(input())
if a3 > 0:
  print('1')
elif a3 == 0:
  print('0')
else:
  print('-1')
#B1
b1list = []
print("Give two numbers:")
for counter in range(0, 2):
  b1 = int(input())
  b1list.append(b1)
b1list = sorted(b1list)
print(b1list[0])
#B2
b2 = int(input)
print("Your age is", b2)
if b2 < 18:
  print("You're a minor")
elif b2 > 100:
  print("You're a geezer")
#B3
b3 = int(input("How many children?"))
if b3 > 10:
  print("You owe:", b3 * 2 + 50)
else:
  print("You owe:", b3 * 1.5 + 40)
#C1
months = ['Invalid', 'January',  'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
c1 = int(input("Month number:"))
if c1 < 0 or c1 > 12:
  print('Invalid')
else:
  print(months[c1])
#C2
c2 = int(input())
scholarships = ['Dean\'s award for $500', 'Chancellor\'s scholarship for $2000', 'President\'s scholarship for $3000']
if c2 > 70 and c2 < 80:
  print('You are eligible for the', scholarships[1])
elif c2 > 80 and c2 < 90:
  print('You are eligible for the', scholarships[1])
elif c2 > 90:
  print('You are eligible for the', scholarships[2])
elif c2 > 100 or c2 < 0:
  print('Nice try, but I thought of that already')

#A1 Vaccination
Vaccination = True
if not Vaccination:
  print("Please vaccinate your dog")
#A2
num = int(input("Enter a number:"))
if num >= 0 and num <= 100:
  print("This is between 1 and 100")
else:
  print("This is not between 1 and 100")
#A3

#A4
insured = True
licensed = True
if licensed and insured:
  print("You may drive")
else:
  print("You may not drive")

#B1
score = 50
time = 30
if score >= 50 and time >= 30:
  print("Level Up!")
else:
  print("Need more time!")

#B2
height = 53
age = 7
if age < 7:
  print("Age is too low")
if height < 53:
  print("Height is too low")
if age >= 7 and height >= 53:
  print("You can go on the slide!")

#B3
int1 = 3
int2 = 5
int3 = 7
integers = sorted([int1, int2, int3])
print(integers[0])

#C1
vowels = ['a', 'e', 'i', 'o', 'u']
letter = 'i'
if letter in vowels:
  print("Vowel")
else:
  print("Consonant")

#C2
goodMonths = ['September', 'November', 'December']
currentMonth = input('Date:')
currentMonth = currentMonth.split(' ')
currentDay = int(currentMonth[1])
currentMonth = currentMonth[0]
if currentMonth in goodMonths:
  print("Good!!!!")
else:
  print("Wait a few months")


