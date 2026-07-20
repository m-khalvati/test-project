# Get Information From User
print("hi there, welcome to our program please enter your information \n")
Name = input("please enter your name : \n> ")
National_Code = input("enter your National Code : \n> ")
Age = int(input("enter your Age : \n> "))

# print the information
print("\n\n################################")
print(
    f"your submitted data : \n Name : {Name} \n National_Code : {National_Code} \n Age = {Age}"
)
print("################################\n")

# using mathematical operators
Random_Number = 2
print("\n//////////////////////////////////")
print(f"""Your Age With Operators:
        +2 = {Age+2}, -2 = {Age-2},
        /2 = {Age/2}, *2 = {Age*2},
        //2 = {Age//2}, %2 = {Age**2},
        **2 = {Age**2}""")
print("//////////////////////////////////\n")

# check age validity
if Age >= 18 and Age <= 30:
    print("your age is between 18 and 30")
else:
    print("your age is not between 18 and 30")
