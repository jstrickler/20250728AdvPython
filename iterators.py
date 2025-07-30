colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in reversed(colors):
    print(color)
print()

rcolors = reversed(colors)
print(f"{rcolors = }")
print()

for i, color in enumerate(colors):
    print(i, color)
print()
print(f"{list(enumerate(colors)) = }")
print()

colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors:
    print(color)
