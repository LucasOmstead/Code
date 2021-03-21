x = input()
newstring = []
for counter in range(0, len(x)-1):
  if counter%2 == 0:
    newstring.append(x[counter])

newstring = ''.join(newstring)
print(newstring)

y = input()
uniques = []
for counter in range(0, len(y)):
  uniques.append(y[counter])
for counter in range(0, len(y)):
  if y[counter] in uniques:
    if y.count(y[counter]) <2 :
      print(y[counter])

      break
  else:
    pass

print(y)
print(uniques)

chant = 'oh yes, cause we are the best'
print(chant[5:9])