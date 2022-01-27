import os

# Change image format. Make sure you run this before doing the labels!
path = r'E:\AI\opencv_contest\new_images'
files = os.listdir(path)

name = 2070

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(name) + '.jpg'])))
    name += 1
