#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:52:30 2020

@author: asher
"""

## Run openSmile on a flie
## 
## ./SMILExtract -C conf/emobase_25ms_file_names_csv.conf  -I example-audio/opensmile.wav -O emobase.csv
##

import glob
import shutil
import os


conf_file ="conf/emobase_25ms_file_names_csv.conf" 
audio_path="example-audio/*"
cvs_file="features.csv"

for file in glob.iglob (audio_path):
    print("Execoting features from", file)
    cmd = "./SMILExtract " +" -C " + conf_file +" -I " + file +" -O " +cvs_file
    os.system(cmd)
print("Done")



