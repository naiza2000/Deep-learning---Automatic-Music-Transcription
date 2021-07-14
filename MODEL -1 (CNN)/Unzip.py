import glob
import os
import librosa
import numpy as np
from shutil import copyfile
import pretty_midi

startpath='MAPS'
subfolder = 'MUS'
destpath = 'Tempdata'
c=0
files = [f for f in os.listdir('MAPS') ]
for f in files:
    fpath=os.path.join(startpath,f,f,subfolder)
    subfiles = [f1 for f1 in os.listdir(fpath)]
    if(c<6):
        subdestpath='train'
    elif(c>=6 and c<8):
        subdestpath = 'test'
    else:
        subdestpath = 'val'
    
    dest =os.path.join(destpath,subdestpath)
    c=c+1
    for f1 in subfiles:
        if(f1.endswith('wav') or f1.endswith('mid')):
            destfile= os.path.join(dest,f1)
            filepath = os.path.join(fpath,f1)
            copyfile(filepath, destfile)
            print("Saved",f1 ,"in",subdestpath)
        