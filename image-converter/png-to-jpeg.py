# Initial .png size = 8.75KB

from PIL import Image

img = Image.open('testimg.png')
img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
img.save("comp.png", optimize=True)