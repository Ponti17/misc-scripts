import os
import sys
import shutil

name = sys.argv[1]

if len(name) < 3:
    print("Filename must be at least 3 characters long.")
    exit()

cwd = os.getcwd()
path = os.path.join(cwd)
files = os.listdir(path)

# Zero indexing
for i in range(0, len(files)):
    print("Renaming " + files[i] + " to " + name + "-" + str(i) + ".pdf")
    shutil.move(os.path.join(path, files[i]), os.path.join(path, name + "-" + str(i) + ".pdf"))