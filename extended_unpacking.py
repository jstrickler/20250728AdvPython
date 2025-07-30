m = [1, 2, 3, 4, 5, 6]

a, b, *c = m
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
print('-' * 60)

a, *b, c = m
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
print('-' * 60)

*a, b, c = m
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', 'rmail', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, *product, dob in people:
    print(last_name, product)
print('-' * 60)

