import csv
import os
from PIL import Image



descriptions_file = "path_to/test_labels.csv"  # path to csv file

with open(descriptions_file,'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    for idx, row in enumerate(lines):
        if idx == 0:
            lines[idx] = ["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"]
        else:
            exists = os.path.isfile('Path_to_training_hand_images/'+row[0]+".jpg")
            if exists and row[2]=="/m/0k65p":   #filters the file by hand’s code

                with Image.open('Path_to_training_hand_images/'+row[0]+".jpg") as img:
                    width, height = img.size
                    lines[idx] = [row[0]+".jpg", width, height, "Human_hand", round(float(row[4])*width), round(float(row[6])*height), round(float(row[5])*width), round(float(row[7])*height)]
            else:
                lines[idx] = [""]


with open(descriptions_file, 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)


readFile.close()
writeFile.close()
