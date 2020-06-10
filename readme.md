# OpenSMILE Features extraction

**OpenSMILE** "world-class audio analysis toolkit" 

This python script runs over all the .wav files in a folder and creates CSV file that contains columns with all the feature according to the configuration file.

>**Note:** The script is based on **SMILExtract** executable file that was compiling on **Ubuntu 18.04.4 LTS**.
The SMILExtract doesn't recognize wav header for wav files written with librosa
to overcome this problems all files are re-written using pydub lib

Using the *.conf* files in this repo will get CSV that contains:

 1. The wav file name
 2. Frame index
 3. Frame time
 4. All the features defined in the configuration flie

You can create your own configuration file following the *openSMILE-latest-book*
from the [official site](https://www.audeering.com/download/opensmile-2-3-0-zip)

Other good information for making configuration files can be found in:

[https://stackoverflow.com/questions/43555779/how-to-create-custom-config-files-in-opensmile](https://stackoverflow.com/questions/43555779/how-to-create-custom-config-files-in-opensmile)


## CVS Examples

When using *emobase_full_frame_2_csv.conf*  the files head :

|    name                                 |pcm_intensity_sma_variance|pcm_intensity_sma_stdd|
|-----------------------------------------|--------------------------|-------------------------
|'example-audio/media-interpretation.wav' |5.729106e-12              |2.393555e-06          |
|'example-audio/opensmile.wav'            |1.634973e-11              |4.043480e-06          |


When using *emobase_25ms_frames_2_csv.conf*  the files head :

|name                                    |frameIndex|frameTime   |pcm_intensity_sma_variance|
|----------------------------------------|----------|------------|--------------------------|
|'example-audio/media-interpretation.wav'|0         |0.012500    |2.828065e-21              |
|'example-audio/media-interpretation.wav'|1         |0.012500    |9.548435e-21              |
|'example-audio/media-interpretation.wav'|2         |0.020006    |5.578462e-21              |
|'example-audio/media-interpretation.wav'|3         |0.030006    |1.493910e-21              |



