import os

print("The files and the folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
