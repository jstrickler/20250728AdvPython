def rectangle_area(length, width):
    return length * width

print(f"{rectangle_area(5, 10) = }")
print(f"{rectangle_area(4.9, 18.3) = :.2f}")

dimensions = 8, 7
print(f"{rectangle_area(dimensions[0], dimensions[1]) = }")
print(f"{rectangle_area(*dimensions) = }")
print()

args = {
    'filename': 'mydata.txt',
    'max_lines': 100,
    'parse_dates': True,
}

def my_big_science_function(*, filename, max_lines, parse_dates):
    print(filename, max_lines, parse_dates)

my_big_science_function(filename='foo.txt', max_lines=10, parse_dates=False)
my_big_science_function(**args)

