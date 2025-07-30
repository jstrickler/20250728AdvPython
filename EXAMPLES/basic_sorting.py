"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(sorted_fruit)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]
print(f"{sorted(nums) = }\n")

nums_as_strs = sorted(nums, key=str)
print(f"{nums_as_strs = }")

nums = [800, "80", 1000, 32, "-3", 8, 18, "255", 400, 5, 5000]
ints_as_ints = sorted(nums, key=int)
print(f"{ints_as_ints = }")

def sort_as_strings(x):
    sort_value = str(x)
    print(f"comparing {repr(x)} as {repr(sort_value)}")
    return sort_value

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]
sorted_nums = sorted(nums, key=sort_as_strings)

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=str.lower)
print(f"{f2 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def by_month(person):
    dob = person[-1]
    year, month, day = dob.split('-')
    return int(month), int(day)

for person in sorted(people, key=by_month):
    print(person)
print('-' * 60)

# lambda param: (return-value)
for person in sorted(people, key=lambda p: p[-1]):
    print(person)

def spam():
    return 42

x = spam
print(f"{x = }")
print(f"{x() = }")

x = spam()
print(f"{x = }")
