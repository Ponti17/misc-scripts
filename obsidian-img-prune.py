import os

obsidian_dir = r"C:/Obsidian/MainVault"

imgs_in_md = []
imgs = []
imgs_path = []
for root, dirs, files in os.walk(obsidian_dir):
    for file in files:
        if ".obsidian" not in root:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as current_file:
                    lines = current_file.readlines()
                    for line in lines:
                        if line.startswith("!["):
                            imgs_in_md.append(line)
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                imgs.append(file)
                imgs_path.append(os.path.join(root, file))

imgs_to_delete = []
imgs_to_delete_path = []
img_found = False
for i in range(0, len(imgs)):
    img_found = False
    for img_md in imgs_in_md:
        if imgs[i] in img_md:
            img_found = True
            break
    if not img_found:
        imgs_to_delete.append(imgs[i])
        imgs_to_delete_path.append(imgs_path[i])
    
print("Found {} images not referenced in any markdown file.".format(len(imgs_to_delete)))

while True:
    usr_input = input("Delete? Y/N/L(ist): ")
    
    if usr_input.lower() == "y":
        for img in imgs_to_delete_path:
            print(f"Deleting {img}")   
            os.remove(img)
        break
    elif usr_input.lower() == "l":
        for img in imgs_to_delete_path:
            print(img)
    elif usr_input.lower() == "n":
        break
    else:
        print("Invalid input.")   

print("Exiting...")
exit()
    
