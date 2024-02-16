from PIL import Image
import os

obsidian_dir = r"C:/Obsidian/MainVault/University/6.semester"

imgs = []
for root, dirs, files in os.walk(obsidian_dir):
    for file in files:
        if ".obsidian" not in root:
            if file.endswith(".png"):
                print("Compressing {}".format(os.path.join(root, file)))
                img = Image.open(os.path.join(root, file))
                img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
                img.save(os.path.join(root, file), optimize=True)
                
                
