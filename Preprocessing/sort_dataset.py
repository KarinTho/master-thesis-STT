# Author: Karin Thommen
# Purpose: Master Thesis
# Content of file: sort audio data new -> in Train, Test and Validation splits
# Date: April 2023


import pandas as pd
import shutil
import os

# load all data files
train = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/train.tsv",sep='\t')
valid = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/valid.tsv",sep='\t')
test = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/test.tsv",sep='\t')

# get path of train, test and valid in a list
train_path = train["clip_path"].tolist()
test_path = test["clip_path"].tolist()
valid_path = valid["clip_path"].tolist()

print(train_path) # check if it worked


# method to move data that is in a given dataset split to the correct folder.
def move_data(dataset_path, folder):
    dst_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200/data" + "/" + folder

    for path in dataset_path:
        src_path = "/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200/data/all" + "/" + path
        src_folder = path.split("/")[0]
        dst_path_new = dst_path + "/" + src_folder
        if not os.path.exists(dst_path_new):
            os.mkdir(dst_path_new)

        shutil.copy(src_path, dst_path_new)


move_data(test_path, "test")
print("test data copied")

move_data(train_path, "train")
print("train data copied")

move_data(valid_path, "valid")
print("validation data copied")


print("Done")
