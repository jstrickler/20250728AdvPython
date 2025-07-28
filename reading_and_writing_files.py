from getpass import getpass

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:   #  .readline()
        food = raw_line.rstrip() # strip off ' ' '\t'  '\n' '\r'
        print(food)
print('-' * 60)
with open('DATA/breakfast.txt') as breakfast_in:
    contents = breakfast_in.read() # read entire file
    print(f"{contents.lower().count('spam') = }")
print('-' * 60)

flags = [True] * 25
print(f"{flags}")

# print("value is %d" % (value)) # oldest
# print("value is {}".format(value))  # older
# print(f"value is {value}"))  # USE THIS

user_name = input("What is your name? ")
print(f"User name is {user_name}")
pw = getpass("What is the password? ")
print(f"{pw = }")


