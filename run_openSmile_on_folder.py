#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:52:30 2020

@author: asher
"""

## Run openSmile on a folder
##file is resaved with pydub be compatable with openSMLIE
## Example hot to run one flie
## ./SMILExtract -C conf/emobase_25ms_frames_2_csv.conf  -I example-audio/opensmile.wav -O emobase.csv
##

import glob
import shutil
import os
from pydub import AudioSegment
from colorama import Fore, Back, Style 


#conf_file ="conf/ComParE_2016.conf" 
#conf_file="emobase_full_frame_2_csv.conf"
conf_file="emobase_25ms_frames_2_csv.conf"
#audio_path="/home/asher/Dataset/Laryngitis_500ms_48K_16bit/train/0/*"

#---------------------------------
audio_path="/home/linuxu/Data/asher_test/Rd/test/healthy/*/*"
cvs_file="Rd_test_healthy_emobase.csv"

if os.path.exists(cvs_file):
    print(Fore.BLUE+"Deleteing old cvs file") ,print(Style.RESET_ALL)
    os.remove(cvs_file)


for file in glob.iglob (audio_path):
    print(Fore.MAGENTA+"Execoting features from", file),print(Style.RESET_ALL)
    try:
        audio = AudioSegment.from_wav(file)
        audio.export(file,format="wav")
        cmd = "./SMILExtract " +" -C " + conf_file +" -I " + file +" -O " +cvs_file
        os.system(cmd)
    except : print (Fore.YELLOW+ file," is empty !") ,print(Style.RESET_ALL) 
        
print("Done")


