import os
import numpy as np
from pathlib import Path
from PIL import Image


#defining all the paths
dataset_path = Path(r"D:\VisDrone2019-MOT-val")
anno_dir = dataset_path / "annotations"
seq_dir = dataset_path / "sequences"
labels_dir = dataset_path / "labels"

#we are looping through every annotation file
for anno_file in anno_dir.glob("*.txt"): #glob("*.txt") finds every .txt files inside annotations
    seq_name = anno_file.stem #we are removing the .txt part
    seq_path =  seq_dir / seq_name
    #creating the output folder (YOLO labeles will be stored here)
    output_dir = labels_dir / seq_name
    anno_path = output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    #we are now reading image dimemnsions to normalise the visdrone values as per YOLO
    #we only see the first image bcz vizdrone dataset actually contains frames of sequences, so every frame has same dim.
    first_image = sorted(seq_path.glob("*.jpg"))[0]
    img = Image.open(first_image)
    img_w,img_h = img.size

    #we are now reading the annotation file, and converting them 1,2,3 to ['1','2','3']
    with open(anno_file, 'r') as f:
        rows = [line.strip().split(',') for line in f.readlines()]


    #we group annotations by frame bcz visdrone stores all frames in one file
    #therefore we are creating a group dictionary
    groups = {}
    for row in rows:
        key = row[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(row)
    print(len(groups))

    #we are keeping only the person classs
    filtered_groups = {}
    for frame_idx, frame_rows in groups.items():
        person_rows = []
        for row in frame_rows:
            if row[7] == '1' or row[7] == '2':
                person_rows.append(row)
        if len(person_rows)>0:
            filtered_groups[frame_idx] = person_rows
    print(f"Frames with persons: {len(filtered_groups)}")


    # here we are generating the YOLO label files
    for frame_idx, frame_rows in filtered_groups.items():
        with open(anno_path/f"{int(frame_idx):07d}.txt", 'w') as f: #creates the label file
            for row in frame_rows:
                x,y,w,h = int(row[2]), int(row[3]), int(row[4]), int(row[5]) #extract the bounding bocx
                #visdrone format : frame_idx, targer_id, x, y, w, h, score, class, turncation, occulsion
                #YOLO format x_center, y_center, width, height
                #converting visdrone to YOLO format
                x_center = (x + w/2) / img_w 
                y_center = (y + h/2) / img_h
                w_norm = w / img_w
                h_norm = h / img_h
                cls = int(row[7])-1 #bcz YOLO classes starts at 0, so visdrone class 1 becomes yolo class 0

                #writing the yolo label
                f.write(f"{cls} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")
       
        

        
