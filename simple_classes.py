colors = list()   # list colors = new list();
cities = list()
cities.append("Durham")
values = list([1, 2, 3, 4])
# colors: instance of list class
# colors.append()  :  instance method (passed the obj)

x = 5    #   x = int(5)

print("foo bar".split())
#  ",".join(list_of_strings)

class Dog:
    def bark(self, bark_type):
        print(f"{self = }")
        print(f"{bark_type}! {bark_type}!")

d1 = Dog()   # Dog.__init__(...)
d2 = Dog()
d1.bark("woof") # obj is automagically passed as 1st argument
d2.bark("yip")
x = 5


