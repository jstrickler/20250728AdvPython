import os
#  grep xyz foo.txt bar.txt ...

#  pos, *optpos, named, **optnamed
#  pos, *, named, **optnamed
#  *, name1, name2

def grep(search_term, *file_paths, show_file_name=False):
    for file_path in file_paths:
        with open(file_path) as file_in:
            file_name = os.path.basename(file_path)
            for raw_line in file_in:
                if search_term in raw_line:
                    if show_file_name:
                        print(file_name, end=" ")
                    line = raw_line.rstrip()  # remove \n
                    print(line)

grep('pig', 'DATA/words.txt', 'DATA/alice.txt', show_file_name=True)
print('-' * 60)

file_list = ['DATA/parrot.txt', 'DATA/presidents.txt']
grep('ush', *file_list, show_file_name=True)

