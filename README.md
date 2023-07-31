# master-thesis-STT
Author: Karin Thommen 

Usage: Master Thesis at UZH (University of Zurich) 

Date: February - August 2023

Abstract: Translators, voice recordings, and voice control are often pre-installed on mobile devices to make everyday life easier. However, Swiss German speakers must use standard German or English when using speech recognition systems. The latest research shows that most of these systems are trained and evaluated on prepared speech. It remains an open question how these speech-to-text systems behave if they are applied to spontaneous speech, which consists of incomplete sentences, hesitations, and fillers. This can be summarised in the following research question: How does a pre-trained speech model fine-tuned on prepared speech behave differently compared to a model that is fine-tuned on spontaneous speech? Differences in speech styles lead to the assumption that performance drops when it comes to spontaneous speech. To assess the differences between prepared and spontaneous speech, two state-of-the-art pre-trained multilingual models were fine-tuned on the corresponding data. One is XLS-R developed by Facebook and proposed
in 2022. Another model is Whisper by OpenAI, proposed in 2023. Surprisingly, the results of both models disprove the hypothesis, as they perform better on spontaneous speech. Multiple improvement techniques were evaluated on their impact on the models. On the one hand, increasing the size of the data set significantly increases performance. However, one main issue in automatically transcribing Swiss German is finding the correct word boundaries. As many errors occur at the character level, it remains open which evaluation metric is the most appropriate for spontaneous speech and a low-resource language like Swiss German.

## Table of Contents
  * [Folder: Preprocessing]
  * [Folder: Prepared Speech](#folder--prepared-speech)
    + STT_1_XLSR_V1
    + STT_1_XLSR_V2
    + STT_1_XLSR_V3
    + STT_2_Whisper_V1
    + STT_2_Whisper_V2
    + STT_2_Whisper_V3
    + STT_2_Whisper_V4
  * [Folder: Spontaneous Speech]x
    + STT_3_Spont_Whisper_V1
    + STT_3_Spont_Whisper_V2
    + STT_3_Spont_Whisper_V3
    + STT_3_Spont_Whisper_V4
    + STT_3_Spont_Whisper_V5
    + STT_3_Spont_Whisper_V6
    + STT_4_Spont_XLSR_V3
  * PreAnalysis.ipynb
  * Testing.ipynb


## Datasets
### SDS-200 
The dataset was provided from SwissNLP in the scope of this master thesis. The audiofiles and the transcripts of the corpus were used to train the model on prepared speech. 

### Schawinski
The dataset was provided by Tanja Samardzic (UZH). The audiofiles and the transcripts of the corpus were used to train the model on spontaneous speech. 

## Files 
### Folder: Prepared Speech
#### XLSR 
All files containing "XLS-R" in their filename use the Wav2Vec XLS-R model from Facebook. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. 

#### Whisper
All files containing "Whisper" in their filename use the Whisper model from OpenAi. 
There exist different versions of the usage of the model. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. 


