

* EEG 

The preprocessed EEG files are divided into stages (read,translate,see,update). Corresponding to each stage, sentence-wise zipped EEG data corresponding to participants can be found. For each sentence (eg S001.json), the keys are comprised of participants who saw the sentence (P05,...) and for each participant, the data is presented in the following format: {time_stamp:[EEG data]}. Here EEG data corresponds to the raw reading from the four electrodes ([sensor1,sensor2,sensor3,sensor4]).

* Gaze

For the gaze data, the structure is similar to the EEG. However for the data, corresponding to each time stamp, there are two corresponding data items: {signal,flag}. Here signal points to the position of the eye as recorded on the screen. The flag here corresponds to if the signal was captured in the middle of a fixation (f) or a saccade (s) or in the absence of both (n).

* Translations
This contains the transcripts of the translations madee by participants in stages 2 and 4. Corresponding to every participant, the odd numbered lines contain the translation made during the translations without looking at the pictures (Stage 2) and the even numbered lined contain the translation made while looking at the pictures (Stage 4). 
** For all the odd numbered lines the format of the annotation is:
<sentence_id>	<stage>	<modification_flag>	<translation>
Here the <modification_flag> indicates if the participant chose to change the translation (c) or keep it the same (s) during Stage 3. The value of 'n' in the <modification_flag> indicates that the participants did not explicitly indicate their choice in Stage 3.
** For all the even numbered lines the format of the annotation is:
<sentence_id>	<stage>	<translation>

