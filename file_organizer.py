import os
import shutil

file = r"C:\Users\user\OneDrive\Desktop\Test_File"

list = os.listdir(file)

scheme = {
    "Pictures": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mov"]
}

for l in list:
    #skip folders
    if os.path.isdir(os.path.join(file, l)):
        continue

    file_name, file_extension = os.path.splitext(l)
    
    for x, y in scheme.items():
        if file_extension in y:
            target_path = os.path.join(file, x)

            if not os.path.exists(target_path):
                os.makedirs(target_path)

            source = os.path.join(file, l)
            destination = os.path.join(target_path, l)
            shutil.move(source, destination)
                
            print(f"{l} moved to the {x} file.")
            break