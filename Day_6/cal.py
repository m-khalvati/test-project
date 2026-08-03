def add(num1, num2):
  print("add :", num1 + num2)

def sub(num1, num2):
  print("sub :", num1 - num2)

def pow(num1, num2):
  print("pow :", num1 ** num2)

def div(num1, num2):
  try:
    print("div", num1 / num2)
  except ZeroDivisionError:
    print("divide to zero not allowed")