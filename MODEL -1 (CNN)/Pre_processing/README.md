# Preprocessing </br>
Three Methods are used for processing the raw input signal:
## 1.STFT-
We need to analyse the signal frequencies in the time domain. The Short Time Fourier Transform generates the output in the time domain giving a 2D array
with complex valued frequencies as one axis and time as the other.
The number of samples in each window is taken to be 502 for the output to fit our model input shape.
The hop length is taken as 256.



## 2.CQT-
In this transform, the distance between the frequency bins is varied exponentially. As the octaves of a note vary in an exponential relation, the spacing between the octaves of a note is nearly constant in a CQT. The output is a 2D vector of complex
values with one axis/dimension representing time and the other, frequency. We have taken the number of bins as 252, bins every octave as 36.
The hop length is taken as 512.

## 3.MEL-
In the Mel scale, the same difference between any 2 Mels corresponds to a perceptually
similar difference in the pitch. Therefore the signal is analyzed in another scale, Mel scale.
This is done by applying a Mel filter to the output of our original STFT.
The number of samples in each window taken is 2048.
The hop size of each window is 512.
Number of Mel bands taken are 252.

### For X_train
The 2D array obtained after applying the transforms on all data is stitched together to make
one .npy file. The 2D array from each .wav file is concatenated along another axis to make it 3-Dimensional. The window width for splicing the 2D array and concatenating the rest along the third dimension is taken as 94 samples. The kernel size in the CNN Model 1 is taken as 7. Zero padding is applied at the ends of the frequency axis in eatch batch to avoid information loss during convolution which makes the size to a net total of 100. Although this is sufficient, a CNN model needs a 4D array as input of
format (batch size, height, width, depth). Hence the dimension of the array is increased by 1, in particular it is the width that is created ( of value 1).
### For Y_train
For the label files we convert the .mid files into piano roll representation. We store
it as an array with two axes. X axis represents time and Y axis repersents frequency.
The values of the array are 1 when the frequency is present at that particular time and 0 if it
is not.
