# Author: Karin Thommen
# Purpose: Master Thesis
# Content of file: Make metadata file for huggingface dataset: SDS 200
# Date: April 2023

import pandas as pd
import csv

# SDS-200: load all splits
train = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/train.tsv",sep='\t')
valid = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/valid.tsv",sep='\t')
test = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200-files/SDS-200 Corpus/splits/test.tsv",sep='\t')

# make metadata file to save dataset on huggingface hub
# format of file: path, transcript

def get_list(data, split):
    audio_list = data.clip_path.values.tolist() # convert the column to a list
    audio_list = ["data/" + split + "/" + s for s in audio_list]
    sentence_list = data.sentence.values.tolist()
    canton_list = data.canton.values.tolist()
    duration_list = data.duration.values.tolist()
    return audio_list, sentence_list, canton_list, duration_list


def make_metafile(train, test, valid):
    audio_train, sentence_train, canton_train, duration_train = get_list(train, "train")
    audio_test, sentence_test, canton_test, duration_test = get_list(test, "test")
    audio_valid, sentence_valid, canton_valid, duration_valid = get_list(valid, "valid")

    with open('/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/SDS-200/data/metadata.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["file_name", "transcription", "canton", "duration"])
        writer.writerows(zip(audio_train, sentence_train, canton_train, duration_train))
        writer.writerows(zip(audio_test, sentence_test, canton_test, duration_test))
        writer.writerows(zip( audio_valid, sentence_valid, canton_valid, duration_valid))


make_metafile(train, test, valid) #make metafile for SDS 200
