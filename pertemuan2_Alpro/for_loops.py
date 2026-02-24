#for_loops :cara 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#cara 2
for x in "banana":
  print(x)
#cara 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#cara 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#cara 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#cara 6
for x in range(6):
  print(x)
#cara 7
for x in range(2, 6):
  print(x)
#cara 8
for x in range(2, 30, 3):
  print(x)
#cara 9
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#cara 10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#cara 11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#cara 12
for x in [0, 1, 2]:
  pass
