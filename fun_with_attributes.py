# getattr()
# setattr()
# hasattr()
# delattr()

from president import President

p = President(2)
print(f"{p = }")
attr_name = "last_name"
if hasattr(p, attr_name):
    value = getattr(p, attr_name)
    print(f"{value = }")
else:
    print("no such attribute")

for attribute in dir(p):
    if attribute.startswith('_'):
        continue
    attribute_value = getattr(p, attribute)
    print(attribute, attribute_value)
print('-' * 60)

class Dog:
    pass

d = Dog()

def woof(self):
    print("woof woof")

setattr(Dog, "bark", woof)
d.bark()