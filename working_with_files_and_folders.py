import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = "DATA/alice.txt"
file_path = f"{FOLDER}/{FILE_NAME}"
file_path = FOLDER + "/" + FILE_NAME
file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")
file_size = os.path.getsize(file_path)
print(f"{file_size = }")
raw_time_stamp = os.path.getmtime(file_path)
print(f"{raw_time_stamp = }")
file_time_stamp = datetime.fromtimestamp(raw_time_stamp)
print(f"{file_time_stamp = }")
print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")
abs_path = os.path.abspath(file_path)
print(f"{abs_path = }")
print(f"{os.path.basename(abs_path) = }")
print(f"{os.path.dirname(abs_path) = }")
print(f"{os.path.split(abs_path) = }")
print(f"{os.path.splitext(abs_path) = }")
