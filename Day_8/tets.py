#test 1
class Std:
  def __init__(self, name):
    self.f_name = name

  def Say_hello(self, friend):
    print(self.f_name,"say hello to", friend)


s1 = Std("Ali")
s1.Say_hello("mohammad")

# print(f"name : {s1.f_name} say hello to {s1.f}")
# print(f"age : {s1.age}")
