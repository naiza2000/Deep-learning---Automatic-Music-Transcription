# POST PROCESSING:<br/>
1. Converted 2D Boolean matrix outputed by the RNN Model into a 2D binary piano roll.<br/>
2. Used the MIDIUtil library to create a MIDI file from the piano roll.<br/>
3. Generated a dataframe from the MIDI file using pretty_MIDI library.<br/>
4. Created a piano roll representation from the dataframe using Matplotlib.<br/>




// generate midi file from each trained model, upload them with convention -> MIDI_file_stft.mid,, etc. 
// Upload the original file as well. 
