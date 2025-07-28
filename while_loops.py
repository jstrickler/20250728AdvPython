i = 0
while i < 3:
    print(i)
    i += 1
print('-' * 60)
while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    if name == '':
        continue
    print(f"Thanks, {name}")