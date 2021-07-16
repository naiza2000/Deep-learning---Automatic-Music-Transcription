import glob
import os
import librosa
import numpy as np
import shutil
import pretty_midi

startpath='Data'
destpath = 'TempPreprocessing'
subfolder='MUS' 
RangeMIDInotes=[21,108]
sr=44100.
bins_per_octave=36
n_octave=7
val_rate=1./7
pretty_midi.pretty_midi.MAX_TICK = 1e10
n_bins=n_octave*bins_per_octave
hop_length = 512
win_width = 32
kernel_size=7
overlap=True

def midi2mat(midi_path_train, length, CQT_len, sr, RangeMIDInotes=RangeMIDInotes):
    midi_data = pretty_midi.PrettyMIDI(midi_path_train)
    pianoRoll = midi_data.instruments[0].get_piano_roll(fs=CQT_len * sr/length)
    Ground_truth_mat = (pianoRoll[RangeMIDInotes[0]:RangeMIDInotes[1] + 1, :CQT_len] > 0)
    return Ground_truth_mat

files = [f for f in os.listdir('Data') ] #contains train test and val folder
for f in files:
    print(f)
    j=0
    k=0
    fpath=os.path.join(startpath,f)
    print(fpath)
    subfiles = [f1 for f1 in os.listdir(fpath)]    
    for f1 in subfiles:
        ffile=os.path.join(fpath,f1)
        file_name,file_extensions=os.path.splitext(f1)
        if file_extensions == '.txt':
            continue
        if file_extensions==".mid":
            ffile=os.path.join(fpath,file_name+'.wav')
        #loading the file
        x,sr = librosa.load(ffile,sr=sr)
        #applying CQT transform
        cqt_file = librosa.cqt(x,sr=sr,fmin=librosa.note_to_hz('A0'),hop_length = hop_length,n_bins=n_bins,bins_per_octave=bins_per_octave,scale=False) 
        cqt=np.transpose(np.abs(cqt_file))
        midi_file = os.path.join(fpath,f1)
        if file_extensions==".wav":
            midi_file = os.path.join(fpath,file_name+'.mid')
        #converting midi files to array
        Ground_truth_mat=midi2mat(midi_file, len(x), cqt.shape[0], sr, RangeMIDInotes=RangeMIDInotes)
        midi_train = np.transpose(Ground_truth_mat)
        
        #midi length<CQT length, cut CQT
        if midi_train.shape[0]<cqt.shape[0]:
            cqt=cqt[:midi_train.shape[0],:]
        if file_extensions == ".wav":
            ofolder = 'wav'
            subname = 'CQT'
        elif file_extensions == ".mid" :
            ofolder = 'mid'
            subname = 'label'
        opath = os.path.join(destpath,f,ofolder,file_name)+subname+'.npy'
        # saving individual numpy arrays
        if file_extensions == ".wav":
            np.save(opath,cqt)
        elif file_extensions == ".mid":
            np.save(opath,midi_train)
        print('Preprocessed',f1)   
        
        #adding padding and dimension
        matrix = np.array(np.load(opath))
        l=matrix.shape[0]
        cut_matrix=[]
        nb_win=int(l/win_width)   #integer division=floor
        if not overlap:
            for i in range(nb_win):
                cut_matrix.append(matrix[i*win_width:(i+1)*win_width,:])
        else:
            w=matrix.shape[1]
            matrix_1=np.concatenate([np.zeros([int(kernel_size/2),w]),matrix,np.zeros([int(kernel_size/2),w])],axis=0)  #padding
            cut_matrix = []
            for i in range(nb_win):
                cut_matrix.append(matrix_1[i * win_width:(i + 1) * win_width+kernel_size-1,:])    #0-104,100-204,...
        cut_matrix = np.asarray(cut_matrix)
        #concatenating All the files together
        if file_extensions == ".wav":
            if j == 0:
                X = cut_matrix
            else:
                X = np.concatenate((X,cut_matrix),axis=0)
            j=j+1
        elif file_extensions == ".mid":
            if k == 0:
                Y = cut_matrix
            else:
                Y = np.concatenate((Y,cut_matrix),axis=0)
            k=k+1   
        print('Joined',f1)
    #saving the conactenated arrays to a folder
    opath1= os.path.join(destpath,f,"Xfinal")+'.npy'
    opath2= os.path.join(destpath,f,"Yfinal")+'.npy' 
    np.save(opath1,X)
    np.save(opath2,Y)
    print('Saved Xfinal in',f)     
    print('Saved Yfinal in',f)   
