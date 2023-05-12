# Author: Karin Thommen
# Purpose: Master Thesis
# Content of file: Make metadata file for huggingface dataset: Schawinski
# Date: April 2023

import pandas as pd
import csv
from sklearn.model_selection import train_test_split

# Schawinski: load all data
all_data = pd.read_csv("/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski_data/output/schawinski.csv")
all_data_filtered = all_data.loc[(all_data['no_relevant_speech']== 0)]
all_data_filtered = all_data_filtered.loc[(all_data_filtered['speech-in-speech']== 0)]
train, test = train_test_split(all_data_filtered, test_size=0.2)
train, valid = train_test_split(train, test_size=0.2)

print(len(train), len(test), len(valid))

# make metadata file to save dataset on huggingface hub
# format of file: path, transcript

def get_list(data, split):
    audio_list = data.utt_id.values.tolist() # convert the column to a list
    audio_list = ["data/" + split + "/" + s + ".wav" for s in audio_list]
    sentence_list = data.transcription.values.tolist()
    duration_list = data.duration.values.tolist()
    return audio_list, sentence_list, duration_list


def make_metafile(train, test, valid):
    audio_train, sentence_train, duration_train = get_list(train, "train")
    audio_test, sentence_test, duration_test = get_list(test, "test")
    audio_valid, sentence_valid, duration_valid = get_list(valid, "valid")

    with open('/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski/metadata.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["file_name", "transcription", "duration"])
        writer.writerows(zip(audio_train, sentence_train, duration_train))
        writer.writerows(zip(audio_test, sentence_test, duration_test))
        writer.writerows(zip( audio_valid, sentence_valid, duration_valid))


make_metafile(train, test, valid) #make metafile for Schawinski
