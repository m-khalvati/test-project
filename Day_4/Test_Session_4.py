# std = ["ali", "ali3", "ali4"]
# print(std[-1])
# print(len(std))
# for s in std:
#   print(s)

# print(std.sort())
# # print(a)
# std.clear()
# std.reverse()

# test 1
# num = [6,11,15,91,12]

# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.clear()
# print(num)

# days = ("sunday", "monday")
# print(days.count("s"))

# set = {1,2,3,3}
# set.add(7)
# set.remove(2)
# print(set)

stu = {"name":"ali", "age":22}
del stu["age"]
print(stu["name"])
stu["name"] = "a"
print(stu)
print(stu.keys())
print(stu.values())
print(stu.items())

for key,value in stu.items():
  print(key," ", value)