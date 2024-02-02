import os
import sys
import shutil

if len(sys.argv) < 3:
    print("Usage: python script.py <folder> <template>")
    sys.exit(1)

folder = sys.argv[1]
template = sys.argv[2]

if template == '.' or template == 'default':
    template = "assignment-template.tex"

template_path = r"c:\git\latex-templates"
source = os.path.join(template_path, template)
cwd = os.getcwd()
dest = os.path.join(cwd, folder)

if not os.path.exists(dest):
    print("Creating directory " + dest)
    os.makedirs(dest)

shutil.copy(source, dest)
shutil.move(os.path.join(dest, template), os.path.join(dest, folder + ".tex"))
os.mkdir(dest + "/imgs")
print("Template copied to " + dest)