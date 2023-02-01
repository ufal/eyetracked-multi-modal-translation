# EMMT Recordings Preprocessed

In this directory, the recordings are reorganized so that all observations of a stimulus of a given type are aggregated and the surrounding stimuli the subject has seen are no longer easily accessible.

EEG and gaze data are divided into the processing stages: READ, TRANSLATE, SEE, UPDATE.

Furthermore, the translations produced by the subjects were manually transcribed and all the surrounding comments were disregarded.

## EEG 

One zipped json file with EEG data is provided for each processing stage (read, translate, see, update) and input sentence (``Sxxx``).

The json contains a dictionary data structure with participants who saw the sentence (P05,...) as the keys.

For each participant, the data is presented in the following format: ``{time_stamp:[EEG data]}``. Here EEG data corresponds to the raw reading from the four electrodes ([sensor1, sensor2, sensor3, sensor4]).

## Gaze

For the gaze data, the files structure is similar to EEG: one file for each stage and input sentence, then a dictionary from participants to list of time-stamped observations.

At each time stamp, a tuple is provided: ``{signal,flag}``. Here ``signal`` points to the position of the eye as recorded on the screen. The ``flag`` indicates if the signal was captured in the middle of a fixation (``f``) or a saccade (``s``) or in the absence of both (``n``).

## Translations

This directory contains the transcripts of the translations made by participants in stages 2 (translate) and 4 (update).
Each file now corresponds to a participant (``Pxx``).

The odd numbered lines contain the translation made during the translations without looking at the pictures (Stage 2) and the even numbered lined contain the translation made while looking at the pictures (Stage 4). 
* For all the odd numbered lines the format of the annotation is:
``<sentence_id>	<stage>	<modification_flag>	<translation>``
Here the <modification_flag> indicates if the participant chose to change the translation (c) or keep it the same (s) during Stage 3. The value of 'n' in the <modification_flag> indicates that the participants did not explicitly indicate their choice in Stage 3.
* For all the even numbered lines the format of the annotation is:
``<sentence_id>	<stage>	<blank column> <translation>``

