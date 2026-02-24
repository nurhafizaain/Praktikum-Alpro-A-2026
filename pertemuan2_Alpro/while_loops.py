#while loops :cara 1
i = 1
while i < 6:
  print(i)
  i += 1
#cara 2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#cara 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#cara 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
