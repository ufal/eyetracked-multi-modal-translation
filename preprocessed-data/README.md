# EMMT Recordings Preprocessed

In this directory, the recordings are reorganized so that all observations of a stimulus of a given type are aggregated. The surrounding stimuli the subject has seen may no longer be easily accessible.

EEG and gaze data are divided into the processing stages: READ, TRANSLATE, SEE, UPDATE.

Furthermore, the translations produced by the subjects were manually transcribed and all the surrounding remarks uttered by the subjects were disregarded.

## EEG 

One json file with EEG data is provided for each processing stage (read, translate, see, update) and input sentence (``Sxxx``).

The json contains a dictionary data structure with participants who saw the sentence (P05,...) as the keys.

For each participant, the data is presented in the following format: ``{time_stamp:[EEG data]}``. Here EEG data corresponds to the raw reading from the four electrodes ([sensor1, sensor2, sensor3, sensor4]).

## Gaze

For the gaze data, the files structure is similar to EEG: one file for each stage and input sentence, then a dictionary from participants to list of time-stamped observations.

At each time stamp, a tuple is provided: ``{signal,flag}``. Here ``signal`` points to the position of the eye as recorded on the screen. The ``flag`` indicates if the signal was captured in the middle of a fixation (``f``) or a saccade (``s``) or in the absence of both (``n``).

## Translations

This directory contains the transcripts of the translations made by participants in stages 2 (Translate) and 4 (Update).
Each file now corresponds to a participant (``Pxx``) and the individual lines are in the order in which the stimuli were presented to the participant.

Each line has the following tab-delimited fields:

- Sentence_ID ... the ID of the sentence
- Original ... the original English text of the source sentence
- Congruency ...indicators if the presented text was ``A``mbiguous or ``U``nambiguous and the presented image was ``R``elated, ``U``nrelated or not provided at all (``N``eutral)
- Choice ... the indication by the subject whether to keep the translation unchanged (``same``) or whether to update it (``changed``)
- Translate ... the full text of the spoken translation in stage 2 (Translate)
- Update ... the full text of the spoken translation in stage 4 (Update)

Here is an example:
```
S004<tab>Some people are standing in the middle of the street lined with motorcycles.<tab>U-R<tab>changed<tab>Nějací lidé stojí ve středu ulice seřazení s motorkami.<tab>Někteří lidé postávají veprostřed ulice obložené motorkami.
```

