import os

STARTING_FOLDER = "."

file_sizes = []
for current_folder, subfolders, file_names in os.walk(STARTING_FOLDER):
    if '.git' in subfolders:
        subfolders.remove('.git')
    # print(current_folder)
    for file_name in file_names:
        if file_name.endswith('.py') and file_name.startswith('c'):
            file_path = os.path.join(current_folder, file_name)
            file_size = os.path.getsize(file_path)
            file_sizes.append((file_size, file_path))
            if file_size < 2000:
                continue
            print(f"{file_size:8,d} {file_name}")

sorted_file_sizes = sorted(file_sizes, reverse=True)
for file_size, file_path in sorted_file_sizes:
    print(file_size, file_path)
top_3 = sorted_file_sizes[:3]
print(f"{top_3 = }")
for file_size, file_name in top_3:
    print(f"deleting {file_name}")