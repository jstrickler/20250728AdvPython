import os

all_lines_count = 0
all_files_count = 0

for current_dir, dir_list, file_list in os.walk('..'):  # start in parent of ANSWERS
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(current_dir, file_name)
            with open(file_path) as file_in:
                try:
                    file_lines_count = len(file_in.readlines())
                    all_files_count += 1
                except Exception as err:
                    print(err)
                    print("FILE NAME WAS", file_path)
            all_lines_count += file_lines_count

print(f"There were {all_lines_count} total lines in {all_files_count} Python files")
