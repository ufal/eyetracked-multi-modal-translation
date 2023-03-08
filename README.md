# Eyetracked Multi-Modal Translation (EMMT)
Release version 1.0

We present Eyetracked Multi-Modal Translation (EMMT), a dataset containing monocular eye movement recordings, audio data and 4-electrode wearable electroencephalogram (EEG) data of 43 participants while engaged in sight translation task supported by an image.

The full description of the experiment design is in the [paper accompanying the EMMT dataset](https://arxiv.org/abs/2204.02905):

```
@article{bhattacharya2022emmt,
  title={EMMT: A simultaneous eye-tracking, 4-electrode EEG and audio corpus for multi-modal reading and translation scenarios},
  author={Bhattacharya, Sunit and Kloudov{\'a}, V{\v{e}}ra and Zouhar, Vil{\'e}m and Bojar, Ond{\v{r}}ej},
  journal={arXiv preprint arXiv:2204.02905},
  url={https://arxiv.org/abs/2204.02905},
  year={2022}
}
```

An analysis of reaction times within the context of the Stroop effect is in [a small analysis paper](https://psyarxiv.com/5qdgr):

```
@article{bhattacharya2022stroop,
   title={Stroop Effect in Multi-Modal Sight Translation},
   author={Bhattacharya, Sunit and Zouhar, Vilém and Kloudová, Věra and Bojar, Ondřej},
   url={psyarxiv.com/5qdgr},
   journal={PsyArXiv},
   year={2022},
}
```

### Description of the data collected

The participants processed inputs in four stages: (1) reading an English sentence aloud, (2) translating it to Czech, (3) observing an image, related or unrelated to the sentence, (4) producing the same or a new translation.

Three kinds of data were recorded during the course of the experiment: eye-tracking (gaze), EEG and audio.

For the experiment, each participant was presented with a set of 32 stimuli, each containing the text of the English sentence and the image. Each such set of 32 stimuli is referred to as a "probe". 20 such probes were used for the purpose of the experiment. EMMT contains the gaze and audio recordings of 43 participants (P01-P43). EEG data of 28 (out of 43) participants was collected and accordingly included in EMMT. 

### Description of the folder structure

This is the overall folder structure used here: 

```
EMMT/
    - probes/
        - probe<xy>
            - P<participant_id>-<order_of_presentation>-S<sentence_id>-<cond>-<cong>-i<image_id>.eeg
            - P<participant_id>-<order_of_presentation>-S<sentence_id>-<cond>-<cong>-i<image_id>.et
            - P<participant_id>-<order_of_presentation>-S<sentence_id>-<cond>-<cong>-i<image_id>.events
            - P<participant_id>-<order_of_presentation>-S<sentence_id>-<cond>-<cong>-i<image_id>.mp3
            - ...
            - probe
        - ...
        - Participants.csv
        - Sentences.csv

    - images/
        - a<image_id>.jpg
        - a...   
        - u<image_id>.jpg
        - u...
        - 100.jpg

    - preprocessed-data/
        - README.md
        - eeg
        - gaze
        - translations
```

#### Raw Data

The folder ``probes/`` contains the raw recordings corresponding to the probes presented to the participants. The probes are numbered in the format:``probe<xy>`` with ``<xy>`` ranging from 01 to 20. 
The details of the 32 stimuli in the probe can be found in the file called ``probe`` inside each ``probe<xy>/`` directory.

Inside each ``probe<xy>/`` directory, there are four types of files corresponding to each stimuli presented to the participants:

- ``.events`` contains the overall timing log
- ``.et`` is the gaze file
- ``.eeg`` is the EEG recording (missing for some participants)
- ``.mp3`` is the recording of the spoken translations and anything else said by the participant or the experiment moderator

The filenames have the following format:
``P<participant_id>-<order_of_presentation>-S<sentence_id>-<cond>-i<cond><image_id>`` and then the file type suffix.

- ``<participant_id>`` corresponds to the unique participant ID accorded to each participant. The anonymized participant names and the <participant_id> corresponding to them can be found in the file ``probes/Participants.csv``.
- ``<order_of_presentation>`` refers to the actual order in which the stimuli were presented to the participant. Note that the stimuli listed in the ``probe`` file were presented in a random order to each participant during the experiment. ``<order_of_presentation>`` contains the information about that ordering.
- ``<sentence_id>`` is the unique ID assigned to the English sentence. All sentences used in the experiment with their IDs can be found in the file ``probes/Sentences.csv``.
- ``<cond>`` refers to the condition captured by the textual stimulus. ``<cond>`` has the values of ``A`` or ``U`` corresponding to an ambiguous or unambiguous sentence, respectively. 
- ``<cong>`` refers to the congruency between the textual stimulus and the visual stimulus. ``<cong>`` has the values of ``C``, ``I`` or ``M`` corresponding to Congruent (text and image are related), Incongruent (text and image are unrelated) and Missing (image is missing, i.e. an empty image shown).
- ``<image_id>`` refers to the ID of the actual image presented to the participant as part of the stimulus. The image ID distinguishes between images serving for ambiguous sentences (``a...``) and unambiguous sentences (``u...``). The images can be found in the ``images/`` directory.

#### Preprocessed Data

The folder ``preprocessed-data/`` contains the data divided into the 4 stages.

The gaze and EEG recordings are in JSON format, the translations produced by the participants are manually transcribed and stored in a simple tab-delimited plain text file. Please see ``preprocessed-data/README.md`` for details on the file formats.

## Authors

* Sunit Bhattacharya
* Věra Kloudová 
* Vilém Zouhar
* Ondřej Bojar

## License

This project is licensed under a Creative Commons Attribution 4.0 International License. - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment

This dataset was created with the support of the NEUREM3 grant (19-26934X) of the Czech Science Foundation.
