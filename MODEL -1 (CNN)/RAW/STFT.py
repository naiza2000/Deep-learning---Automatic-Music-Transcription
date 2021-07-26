import glob
import os
import librosa
import numpy as np
import shutil
import pretty_midi

startpath='Data'
destpath = 'TempData'
subfolder='MUS' 

RangeMIDInotes=[21,108]
n_fft = 512
sr=44100.
bins_per_octave=36
n_octave=7
val_rate=1./7
pretty_midi.pretty_midi.MAX_TICK = 1e10

n_bins= n_octave * bins_per_octave
hop_length = 256
win_width = 32

kernel_size=7
overlap=True

def midi2mat(midi_path_train, length, spect_len, sr, RangeMIDInotes=RangeMIDInotes):
    midi_data = pretty_midi.PrettyMIDI(midi_path_train)
    pianoRoll = midi_data.instruments[0].get_piano_roll(fs=spect_len * sr/length)
    Ground_truth_mat = (pianoRoll[RangeMIDInotes[0]:RangeMIDInotes[1] + 1, :spect_len] > 0)
    return Ground_truth_mat


files = [f for f in os.listdir('Data')]

#fpath is path of different MUS folders

for f in files:
    j=0
    k=0
    print(f)
    fpath=os.path.join(startpath,f)
    print(fpath)
    subfiles = [f1 for f1 in os.listdir(fpath)]    

    for f1 in subfiles:
        mainfile=os.path.join(fpath,f1)

        file_name,file_extensions=os.path.splitext(f1)

        if file_extensions == ".txt":
            continue

        if file_extensions == ".mid":
            mainfile=os.path.join(fpath,file_name+'.wav')

        # if file_extensions == ".mid":
        #     continue
        # mainfile=os.path.join(fpath,f1)
        # if file_extensions == ".wav":
        #     mainfile = f1

        x ,sr = librosa.load(mainfile,sr=sr)

        # -----------------------------------------------------------------------------------------------------------
        fft = np.fft.fft(x)
        spectrum = np.abs(fft)

        # perform stft
        stft = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)[:-1]

        # calculate abs values on complex numbers to get magnitude
        spect = np.transpose(np.abs(stft))
        log_spectrogram = librosa.amplitude_to_db(np.transpose(spect))

        # ------------------------------------------------------------------------------------------------------------
        midi_file = os.path.join(fpath,f1)

        if file_extensions==".wav":
            midi_file = os.path.join(fpath,file_name+'.mid')

        Ground_truth_mat=midi2mat(midi_file, len(x), spect.shape[0], sr, RangeMIDInotes=RangeMIDInotes)
        midi_train = np.transpose(Ground_truth_mat)
        
        #midi length<stft length, cut stft
        if midi_train.shape[0]<spect.shape[0]:
            spect=spect[:midi_train.shape[0],:]
    
        if file_extensions == ".wav" :
            ofolder = 'wav'
            subname = 'STFT'
        elif file_extensions == ".mid" :
            ofolder = 'mid'
            subname = 'label'

        opath = os.path.join(destpath,f,file_name)+subname+'.npy'

        if file_extensions == ".wav":
            np.save(opath,spect)
        elif file_extensions == ".mid":
            np.save(opath,midi_train)

        print('Preprocessed',f1)   
        
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
        os.remove(opath)
        print("Removed",f1)            

        if file_extensions == ".wav":
            if j == 0:
                X = cut_matrix
                # print(cut_matrix.shape)
            else:
                X = np.concatenate((X,cut_matrix),axis=0)
                # print(cut_matrix.shape)
            j=j+1
            
        elif file_extensions == ".mid":
            if k == 0:
                Y = cut_matrix
                # print(cut_matrix.shape)
            else:
                Y = np.concatenate((Y,cut_matrix),axis=0)
                # print(cut_matrix.shape)
            k=k+1
        
        
        print('Joined',f1)
    X = np.expand_dims(X,axis=-2)
    Y = np.expand_dims(Y,axis=-2)
    opath1= os.path.join(destpath,"Xfinal")+'.npy'
    opath2= os.path.join(destpath,"Yfinal")+'.npy' 
    np.save(opath1,X)
    np.save(opath2,Y)

    print('Saved X')     
    print('Saved Y final')

    
    
     

      
                
            

