# number of Factorial for example 3!
n = 3
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    # Factorial start with
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)