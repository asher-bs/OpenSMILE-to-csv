#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:52:30 2020

@author: asher
"""

## This Script will exctrcat openSmile feautres from a configuration file that were tweaked.
## was tested on Ubuntu 18.04 LTS
## all the files are re-saved using pydub be compatable with openSMLIE
##
## Example of exctract feautresr from one flie
## ./SMILExtract -C conf/emobase_25ms_frames_2_csv.conf  -I example-audio/opensmile.wav -O emobase.csv
##


import glob
import shutil
import os
from pydub import AudioSegment
from colorama import Fore, Back, Style


conf_file ="conf/emobase_25ms_file_names_csv.conf" 
audio_path="example-audio/*"
cvs_file="features.csv"


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


