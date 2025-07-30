import os
from pprint import pprint

FOLDER = "../DATA"

file_names = 'alice.txt', 'parrot.txt', 'words.txt'

file_info = {name: os.path.getsize(os.path.join(FOLDER, name)) for name in file_names}

pprint(file_info)

print('-' * 60)

capitals = {'NY': 'ALBANY', 'NC': 'RALEIGH', 'CA': 'SACRAMENTO', 'VT': 'MONTPELIER'}

caps = {state: capital.title() for state, capital in capitals.items()}
pprint(caps)

caps = {capital.title(): state for state, capital in capitals.items()}
pprint(caps)

caps = {capital.title(): (i, state) for i, (state, capital) in enumerate(capitals.items())}
pprint(caps, sort_dicts=False)
