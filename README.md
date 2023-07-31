# master-thesis-STT
**Author:** Karin Thommen 

**Usage:** Master Thesis at UZH (University of Zurich) 

**Date:** February - August 2023

## Abstract: 
Translators, voice recordings, and voice control are often pre-installed on mobile devices to make everyday life easier. However, Swiss German speakers must use standard German or English when using speech recognition systems. The latest research shows that most of these systems are trained and evaluated on prepared speech. It remains an open question how these speech-to-text systems behave if they are applied to spontaneous speech, which consists of incomplete sentences, hesitations, and fillers. This can be summarised in the following research question: How does a pre-trained speech model fine-tuned on prepared speech behave differently compared to a model that is fine-tuned on spontaneous speech? Differences in speech styles lead to the assumption that performance drops when it comes to spontaneous speech. To assess the differences between prepared and spontaneous speech, two state-of-the-art pre-trained multilingual models were fine-tuned on the corresponding data. One is XLS-R developed by Facebook and proposed
in 2022. Another model is Whisper by OpenAI, proposed in 2023. Surprisingly, the results of both models disprove the hypothesis, as they perform better on spontaneous speech. Multiple improvement techniques were evaluated on their impact on the models. On the one hand, increasing the size of the data set significantly increases performance. However, one main issue in automatically transcribing Swiss German is finding the correct word boundaries. As many errors occur at the character level, it remains open which evaluation metric is the most appropriate for spontaneous speech and a low-resource language like Swiss German.

**Remark**: Models described and used in the final version of the thesis are marked with a asterik * containing the name of the model as it is used in the thesis. 

## Table of Contents
  * [Folder: Preprocessing](#folder-preprocessing)
  * [Folder: Prepared Speech](#folder-prepared-speech)
    + STT_1_XLSR_V1
    + STT_1_XLSR_V2
    + STT_1_XLSR_V3
    + STT_2_Whisper_V1
    + STT_2_Whisper_V2
    + STT_2_Whisper_V3
    + STT_2_Whisper_V4
  * [Folder: Spontaneous Speech](#folder-spontaneous-speech)
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
### Analysis
* **PreAnalysis**: Analysis of the data sets.

### Evaluation
* **Testing**: File to test the models on the test set.

### Folder: Preprocessing
* **sort_dataset**: all files starting with this file name are used to sort the data set in train, valid and test folders to load them into via AudioFolder to Huggingface. There exist different code files for the different data sets. 
* **make_metadata**: all files starting wtih this file name are used to make the metadata file that is used to load the data set via AudioFolder to Huggingface. There exist different code files for the different data sets. 
* **load_data_to_huggingface:** ll files starting wtih this file name are used to load the data set via AudioFolder to Huggingface. This code can be used if the metadata file is already in the correct directory and all train, test and validation files are sorted. There exist different code files for the different data sets. 

### Folder: Prepared Speech
**XLS-R**: All files containing "XLS-R" in their filename use the Wav2Vec XLS-R model from Facebook. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. These models are fine-tuned using prepared speech data. 
* **STT_1_XLSR_V1**. XLS-R: Prepared Speech Version 1: XLS-R fine-tuned on a small subset of the prepared speech data set, only for first experiments
* **STT_1_XLSR_V2**. XLS-R: Prepared Speech Version 2: 
  + Version 2.1: XLS-R fine-tuned on the large prepared speech data set, without saving on Huggingface, trained for 6000 steps 
   + Version 2.1: XLS-R fine-tuned on the large prepared speech data set, saved on Huggingface, trained for 4000 steps 
* **STT_1_XLSR_V3**. XLS-R: Prepared Speech Version 3: 
  + Version 3.1: XLS-R fine-tuned on the large prepared speech data set, saved on Huggingface and WandB, trained for 4000 steps *(Thesis: Large prepared speech XLS-R model)
  + Version 3.2: XLS-R fine-tuned on the small prepared speech data set, saved on Huggingface, trained for 6000 steps
  + Version 3.2: XLS-R fine-tuned on the small prepared speech data set, saved on Huggingface, trained for 4000 steps *(Thesis: Comparable prepared speech XLS-R model)

**Whisper**: All files containing "Whisper" in their filename use the Whisper model from OpenAi. 
There exist different versions of the usage of the model. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. These models are fine-tuned using prepared speech data. 

* **STT_2_Whisper_V1**. Whisper: Prepared Speech Version 1: Whisper fine-tuned on a small subset of the prepared
speech data set, only for first experiments
* **STT_2_Whisper_V2**. Whisper: Prepared Speech Version 2:
  + Large Version 2.1: Whisper fine-tuned on the large prepared speech data set, default parameters (save-steps = 100, total batch size = 16, learning rate = 0.00001) *(Thesis: Large default Whisper prepared speech model)
  + Large Version 2.2. Whisper fine-tuned on the large prepared speech data set, for 400 steps (interrupted)
  + Small Version 2.3: Whisper fine-tuned on the small prepared speech data set, default parameters (save-steps = 100, total batch size = 16, learning rate = 0.00001) *(Thesis: Small default Whisper prepared speech model)
* **STT_2_Whisper_V3**. Whisper: Prepared Speech Version 3: unused version, no fine-tuning
* **STT_2_Whisper_V4**. Whisper: Prepared Speech Version 4
  + Large Version 4.1: Whisper fine-tuned on the large prepared speech data set, German language token
  + Small Version 4.1: Whisper fine-tuned on the small prepared speech data set, German language token 
  + Small Version 4.2: Whisper fine-tuned on the small prepared speech data set, no German language token
  + Small Version 4.3: Whisper fine-tuned on the small prepared speech data set, no German language token, fixed pre-processing *(Thesis: Comparable prepared speech Whisper model)

### Folder: Spontaneous Speech
**XLS-R**: All files containing "XLS-R" in their filename use the Wav2Vec XLS-R model from Facebook. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. These models are fine-tuned using spontaneous speech data. 

* **STT_4_Spont_XLSR_V1**. XLS-R: Spontaneous Speech Version 1
  + Spontaneous XLS-R Version 1.1: Comparable XLS-R trained on spontaneous speech for 2000 steps  
  + Spontaneous XLS-R Version 1.2: Comparable XLS-R trained on spontaneous speech for 4000 steps  *(Thesis: Comparable spontaneous speech XLS-R model)

**Whisper**: All files containing "Whisper" in their filename use the Whisper model from OpenAi. 
There exist different versions of the usage of the model. There exist different versions of the model, mainly differing in the way data gets loaded and preprocessed. These models are fine-tuned using spontaneous speech data. 
*  **STT_3_Spont_Whisper_V1**. Whisper: Spontaneous Speech Version 1: Whisper fine-tuned on the spontaneous speech data set. save-steps = 1000 & other default settings of the Whisper model, no german language token
*  **STT_3_Spont_Whisper_V2.1**. Whisper: Spontaneous Speech Version 2: Whisper fine-tuned on the spontaneous speech data set. save-steps = 400, other settings of the comparable Whisper version *(Thesis: Comparable Whisper spontaneous speech)
* **STT_3_Spoint_Whisper_V2.2**. Whisper: Spontaneous Speech Version 2.2: Whisper fine-tuned on the spontaneous speech data set. save-steps = 100 & other default settings of the Whisper model *(Thesis: Default Whisper spontaneous speech)
* **STT_3_Spont_Whisper_V3**. Whisper: Spontaneous Speech Version 3: Whisper fine-tuned on the spontaneous speech data set. save-steps = 1000 & other default settings of the Whisper model and german language token 
* **STT_3_Spont_Whisper_V4_1**. Whisper: Spontaneous Speech Version 4: Whisper fine-tuned on the spontaneous speech data set. save-steps = 400 & other settings of the comparable Whisper version. Additionally, noise is added. 
* **STT_3_Spont_Whisper_V4_2**. Whisper: Spontaneous Speech Version 4: Whisper fine-tuned on the spontaneous speech data set. save-steps = 400 & other settings of the comparable Whisper version. No noise. German language token.
* **STT_3_Spont_Whisper_V5**. Whisper: Spontaneous Speech Version 5: Whisper fine-tuned on the spontaneous speech data set. 
  + Spontaneous Speech Version 5.1: 2000 steps, save-steps = 400, lr=1e-5, dropout = 0.2, and noise, keep punctuation
  + Spontaneous Speech Version 5.2: 4000 steps, save-steps = 400, lr=3e-4, dropout = 0.2, no noise, keep punctuation  
  + Spontaneous Speech Version 5.3: 4000 steps, save-steps = 400, lr=3e-4, dropout = 0.2, no noise, fixed pre-processing, no german language token, keep punctuation 
  + Spontaneous Speech Version 5.4: 4000 steps, save-steps = 400, lr=3e-4, no dropout, no noise, fixed pre-processing, no german language token, keep punctuation *(Thesis: Spontaneous Speech Whisper, Improvement Punctuation)
* **STT_3_Spont_Whisper_V6**. Whisper: Spontaneous Speech Version 6: Whisper fine-tuned on the spontaneous speech data set. 
  + Spontaneous Speech Version 6.1: comparable settings. Add german language to processor and feature extractor and force model to predict in german. Do not delete punctuation and other disfluency information from dataset during preprocessing. Dropout = 0.0  *(Thesis: Spontaneous Speech Whisper, Improvement Disfluency without Dropout)	
  + Spontaneous Speech Version 6.2: comparable settings. Add german language to processor and feature extractor and force model to predict in german. Do not delete punctuation and other disfluency information from data set. Dropout = 0.5
  + Spontaneous Speech Version 6.3: comparable settings. Add german language to processor and feature extractor and force model to predict in german. Do not delete punctuation and other disfluency information from data set. Dropout = 0.1 *(Thesis: Spontaneous Speech Whisper, Improvement Disfluency and Dropout)			