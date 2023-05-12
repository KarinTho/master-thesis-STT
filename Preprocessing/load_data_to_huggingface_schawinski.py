# Author: Karin Thommen
# Purpose: Master Thesis
# Content of file: Load audio data to huggingface
# Date: April 2023

import huggingface_hub
from huggingface_hub import notebook_login
from datasets import load_dataset, Audio, load_metric, load_from_disk, DatasetDict, list_datasets
from datasets import Dataset, Sequence
import soundfile as sf


audio_data = load_dataset("audiofolder", data_dir="/Users/karinthommen/Library/CloudStorage/OneDrive-Persönlich/_UZH/Master/Master_Thesis/Data/Schawinski")

print(audio_data)
print(audio_data["train"][0])

audio_data.push_to_hub("karinthommen/schawinski", private=True)