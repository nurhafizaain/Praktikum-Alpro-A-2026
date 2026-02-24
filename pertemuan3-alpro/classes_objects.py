#Classes Objects :cara 1
class MyClass:
  x = 5

#Cara 2
p1 = MyClass()
print(p1.x)

#Cara 3 
del p1

#Cara 4
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#Cara 5
class Person:
  pass
