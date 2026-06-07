def add(x, y): 
  print(x + y)

def sub(x, y):
  print(x - y)

num1 = float(input("Type your first number: "))
addorsub = input("+ or - ?: ")
num2 = float(input("Type your first number: "))

if(addorsub == "+"):
  add(num1, num2)
elif(addorsub == "-"):
  sub(num1, num2)
else:
  printf("Incorrect format try again!")

