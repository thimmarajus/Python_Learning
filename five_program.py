"""JSON in Python"""

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)

print(y)
"""print(json.dumps({"name": "Jhon", "age": 30}))
x = json.dumps(["apple","bananas"])
print(x)
print(json.dumps(("apple","banans")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))"""
"""# a Python Object (dict):
x = {
 "name": "Srinivasa Thimmaraju",
 "age": 30,
 "city": "New York"
}

# Convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)"""
"""# Some JSON
x = '{ "Name":"Srinivasa Thimmaraju", "age":30, "city":"New York"}'

# Parse X:
y = json.loads(x)

#the result is a Python dictionary:
#print(y)
print(y["age"])"""
""" Built-in Modules in Python"""
"""import platform
x = dir(platform)
print(x)"""
#x = platform.system()
#x = dir(platform)
#print(x)
#import mymodule as mx
#
#a = mx.person1["name"]
#print(a)
#mymodule.greeting("Srinivasa Thimmaraju")
"""class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)"""
#class MyNumbers:
#  def __iter__(self):
#    self.a = 1
#    return self
#
#  def __next__(self):
#    x = self.a
#    self.a += 1
#    return x
#
#myclass = MyNumbers()
#myit = iter(myclass)
#
#mystr = "banana"
#t = iter(mystr)
#print(next(t))
#print(next(myit))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#class MyNumbers:
#  def __iter__(self):
#   self.a = 1
#   return self
#
#  def __next__(self):
#   x = self.a
#   self.a += 1
#   return x
#
#myclass = MyNumbers()
#myiter = iter(myclass)
#
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#mytuple = ("apple", "banana", "cherry")
#mystr = "banana"
#for x in mystr:
# print(x)
#mystr = "banana"
#myit = iter(mystr)
#
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#mytuple = ("apple", "banana", "cherry")
#myit = iter(mytuple)
#
#print(next(myit))
#print(next(myit))
#print(next(myit))
#class person:
#    def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#    def myfunc(abc):
#     print("hello my name is " + abc.name + " \t And my age is" ,abc.age)
#p1 = person("Srinivasa Thimmaraju",33)
#p1.age = 40
#del p1
#print(p1)
#del p1.age
#print(p1.age)
#p1.myfunc()
#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age
#
#  def myfunc(self):
#    print("Hello my name is " + self.name)
#
#p1 = Person("John", 36)
#p1.myfunc()
#class person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age
#
#  def myfunc(self):
#    print("Hello my name is " + self.name)
#
#p1 = person("ThimmarajuSrinivasa", 33)
#p1.myfunc()
#class MyClass:
# x = 5
#p1 = MyClass()
#print(p1.x)
