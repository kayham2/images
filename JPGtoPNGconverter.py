import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]
try:
	os.makedirs(f"{folder}/{new_folder}")
except OSError:
	pass
jpg_array = []
for file in os.listdir(f"{folder}"):
	if file.endswith(".jpg"):
		jpg_array.append(file)
for jpg in jpg_array:
	img = Image.open(f"{folder}/{jpg}")
	new_file_name = jpg.replace(".jpg", ".png")
	print(new_file_name)
	img.save(f"{folder}/{new_folder}/{new_file_name}", "png")

# print(file_array)
# print(folder)
# print(new_folder)
