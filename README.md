# master-thesis-STT
Author: Karin Thommen 
Usage: Master Thesis at UZH (University of Zurich) 
Date: February - August 2023

The goal of this master thesis is the development of a baseline for Swiss German Speech to text for prepared and spontaneous speech to compare the performance of a Automated Speech Recognition system on both types of speech. Moreover, the performance on spontaneous speech should be improved.

## Datasets
### SDS-200 
The dataset was provided from SwissNLP in the scope of this master thesis. The audiofiles and the transcripts of the corpus were used to train the model on prepared speech. 

### Schawinski
The dataset was provided by Tanja Samardzic (UZH). The audiofiles and the transcripts of the corpus were used to train the model on spontaneous speech. 

## Files 
### Folder: XLSR 
The files in this folder use the Wav2Vec XLS-R model. There exist different versions of the usage of the model, mainly differing in the way data gets loaded and preprocessed. 

### Folder: Whisper
The files in this folder use the Whisper model from OpenAi. 
There exist different versions of the usage of the model. The differences between the version can be retrieved from the detailedd descriptions of the different files in the folder. 
