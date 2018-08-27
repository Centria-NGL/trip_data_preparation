import os, fnmatch
from os.path import join
root = r'.\combined'



def findDirs (path = root, filter = ''):
    for root, dirs, files in os.walk(path):
        #for file in fnmatch.filter(files, filter):
        #    yield os.path.join(root, file)
        for dir in dirs:
            yield dir

def findFiles(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(path, file)

def test():
    for i in findDirs(root):
        crnt_dir = join(root, i)
        for file in findFiles(crnt_dir):
            print(file)


if __name__ == "__main__" : test()
