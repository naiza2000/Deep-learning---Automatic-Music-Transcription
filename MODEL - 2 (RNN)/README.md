POST PROCESSING
1)Converted 2D Boolean matrix outputed by the RNN Model into a 2D binary piano roll 
2)Used MIDIUtil library to create a MIDI file from the piano roll
3)Used the MIDI file created to generate a dataframe using the pretty_MIDI library
4)Finally, created a piano roll representation from the dataframe using Matplotlib library
