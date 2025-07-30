
#      pos pos pos
def spam(p1, p2, p3='toast'):
    pass

spam(1, 2, 3)
spam('a', 'b', 'c')
spam(1, 2)
spam('up', 'down')

#      tuple     dict
def uni(*args, **kwargs):
    print(f"{args = }")
    # print(f"{args[1] = }")
    
    print(f"{kwargs.get('country') = }")

    

uni(1, 2, 3)
uni(name="Fred", city="Boston")
uni(1, 2, country="Botswana", color="chartreuse")

count = 35

def toast():
    m = 88
    print(f"{m = }")
    print(f"{count = }")
    
toast()
print(f"{m = }")
