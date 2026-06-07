def add(x, y): 
  return x + y

def sub(x, y):
  return x - y

num1 = input("Type your first number")
addorsub = input("+ or - ?")
num2 = input("Type your first number")

if(addorsub == "+"):
  add(num1, num2)
elif(addorsub == "-"):
  sub(num1, num2)
else:
  printf("Incorrect format try again!")

