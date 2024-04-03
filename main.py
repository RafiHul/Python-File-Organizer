import os

data = os.listdir('/home/muhammad/Downloads')
for i in data:
    if i.endswith('pdf'):
        print(i)