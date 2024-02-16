from PIL import Image
import os

# img = Image.open('testimg.png')
# img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
# img.save("comp.png", optimize=True)

obsidian_dir = r"C:/Obsidian/MainVault"

imgs = []
for root, dirs, files in os.walk(obsidian_dir):
    for file in files:
        if ".obsidian" not in root:
            if file.endswith(".png"):
                imgs.append(os.path.join(root, file))
                
