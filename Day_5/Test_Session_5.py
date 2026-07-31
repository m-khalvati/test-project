# functions 

# test 1
# def multiply(a=1):
#   return a*2

# print(multiply("a"))

# test 2 
a = input("what is your name? ")
b = input("what is your last name? ")
c = int(input("enter First number : "))
d = int(input("enter Second number : "))
def test(a = "null",b = "null", c = 1 , d = 1):
  print(f"your name is {a} and your last name is {b}")
  print(f"First Number + Second Number = {c + d}")

test(a,b,c,d)
