# EMMT Recordings Preprocessed

In this directory, the recordings are reorganized so that all observations of a stimulus of a given type are aggregated. The surrounding stimuli the subject has seen may no longer be easily accessible.

EEG and gaze data are divided into the processing stages: READ, TRANSLATE, SEE, UPDATE.

The translations produced by the subjects were manually transcribed and all the surrounding remarks uttered by the subjects were disregarded.

The directory ``unsplit-preprocessed-probes`` contains the probes before splitting to the four stages but already preprocessed as described below for EEG and Gaze.

## EEG 

One CSV file with EEG data is provided for each processing stage (read, translate, see, update) and input sentence (``Sxxx``).

The filename encodes details on the stimulus, e.g.: ``P03-01-S092-U-R.csv`` means that the participant ``P03`` as the first stimulus (``01``) saw the sentence ``S092`` (which is deemed ``U``nambiguous), and in the See stage, a ``R``elated image was presented.

The CSV has columns with all the recorded signals from the MUSE 2 Headband.

Important remarks:
- MUSE 2 timestamps (the first column) are not of a sufficient resolution, there are sometimes multiple measurements reported at the same millisecond.
- MUSE 2 does some automatic estimation of blinks and jaw clenches; these are reported as lines with only the timestamp in the first column and the corresponding flag in the last column; this estimation does not seem to be reliable.

## Gaze

For the gaze data, the files structure is identical to EEG: one file for each stage and input sentence, same filename convention (e.g. ``P03-01-S092-U-R.csv`` as above).

The CSV has these columns:
- timestamp in 10000ths of a second
- X position of the gaze in screen coordinates (or empty)
- Y position of the gaze in screen coordinates (or empty)
- event indication as estimated by the eye tracker: ``saccade``, ``fixation`` or ``blink``

If the particular stimulus was not recorded, e.g. due to calibration failure, the file is empty.

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

