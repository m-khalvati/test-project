# file = open("name.txt", "w") # x just for create
# file.write("reza")
# file.close()

# file = open("name.txt", "a") # x just for create
# file.write("\nali")
# file.close()

# file = open("name.txt", "r") # x just for create
# print(file.read())
# file.close()

with open ("text.txt", "w") as file:
  file.write("reza")


with open ("text.txt", "a") as file:
  file.write("\nali")


with open ("text.txt", "r") as file:
  print(file.read())