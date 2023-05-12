# Author: Karin Thommen
# Purpose: Master Thesis
# Content of file: sort audio data new -> in Train, Test and Validation splits
# Date: April 2023


import pandas as pd
import shutil
import os

# load all data files
# V1
# all_data = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks/metadata.csv")

# V2
all_data = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks_full/metadata.csv")

# get path
path = all_data["file_name"].tolist()

# method to move data that is in a given dataset split to the correct folder.
def move_data(dataset_path):
    # V1
    # dst_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks/data"
    # V2
    dst_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks_full/data"
    for path in dataset_path:
        src_split = path.split("/")[1]
        # V1
        # src_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks/data/" + path.split("/")[2]
        # V2
        src_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_chunks_full/" + path.split("/")[2]
        dst_path_new = dst_path + "/" + src_split
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path_new)


move_data(path)
print("Done")
