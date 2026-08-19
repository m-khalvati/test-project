# class Animal:
#   def __init__(self):
#     pass

#   def eat(self):
#     print("eat")

#   def sleep(self):
#     print("khoo")


# class Cat(Animal):
#   pass

# cat = Cat()

# cat.eat()

# cat.sleep()

# test 2
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def disp(self):
    print(self.fname)
    print(self.lname)

class Std(Person):
  def __init__(self, fname, lname, age):
    Person.__init__(self,fname, lname)

    self.age = age
  def disp(self):

    # prevent to exp base method
    Person.disp(self)
    print(self.age)


def input_all():
    info = []
    fname = input("please enter your name: ")
    lname = input("please enter last name: ")
    age = input("please enter your age: ")
    info.append(fname)
    info.append(lname)
    info.append(age)
    return info

i = input_all()
s1 = Std(i[0], i[1], i[2])
s1.disp()

