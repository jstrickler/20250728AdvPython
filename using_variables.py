x = 5  #  x = int(5)
y = x
x = 10

thing = None
print(f"{type(thing) = }")

name: str
name = 5
print(f"{name = }")

#  some_name
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
print(f"{fruits[-1] = }")
# print(f"{fruits[22] = }")  INVALID

#  slice  LIST[start-at:stop-before:count-by]
print(f"{fruits[0:3] = }")
print(f"{fruits[:3] = }")
print(f"{fruits[4:11] = }")
start = 3
num_objects = 5
print(f"{fruits[start:start + num_objects] = }")
print(f"{fruits = }")

fruits[2:3] = ['huckleberry', 'buddha hand', 'lychee']
print(f"{fruits = }")

print(f"{fruits[-3:] = }")
print(f"{fruits[1:-1] = }")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

d1 = {}  # empty
d2 = dict(foo=12, bar=13)
print(f"{d2 = }")

print(f"{airports['RDU'] = }")
print(f"{airports.get('ORD') = }")
print(f"{airports.get('RDU') = }")
print(f"{airports.get('ORD', 'NOT FOUND') = }")

print(f"{airports.setdefault('ORD', 'Chicago') = }")
print(f"{airports = }")

more_airports = {'VCE': "Venice", 'FCO': 'Rome'}

airports |= more_airports
print(f"{airports = }")









