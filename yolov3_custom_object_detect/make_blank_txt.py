# Make .txt files for images with no positives
import os

path = r'E:\AI\opencv_contest\not_positives'
for i in os.listdir(path):
    if i[-4:].lower() == '.jpg':
        print('True. Making .txt file')
        open(path + r'\\' + str(i[:-4]) + '.txt', 'w')
