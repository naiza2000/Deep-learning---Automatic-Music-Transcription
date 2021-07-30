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
one .npy file. The 2D array from each .wav file is concatenated along another axis to make it 3-Dimensional. The window width for splicing the 2D array and concatenating the rest along the third dimension is taken as 32 samples. The kernel size in the CNN Model 1 is taken as 7. Zero padding is applied at the ends of the frequency axis in eatch batch to avoid information loss during convolution which makes the size to a net total of 38. Although this is sufficient, a CNN model needs a 4D array as input of
format (batch size, height, width, depth). Hence the dimension of the array is increased by 1, in particular it is the width that is created ( of value 1).
### For Y_train
For the label files we convert the .mid files into piano roll representation. We store
it as an array with two axes. X axis represents time and Y axis repersents frequency.
The values of the array are 1 when the frequency is present at that particular time and 0 if it
is not.

# MODEL

Like our first model, our second model is also a sequential model consisting of 5 stages. The input shape for this model is `(none, 38, 252, 1)` which corresponds to `(Batch No, height, width, depth)`. All five stages comprise of the `Conv2D` layers. In the first two stages `Batch Normalisation` and `Max Pooling` layers have been added after the `Conv 2D` layers. In the third and fourth stages, a `Dropout` layer with `rate=0.5` has been added, which implies that 50% of the total neurons will be randomly dropped in every epoch. 

Since we had added `padding` during pre processing of the data, we kept the same padding to maintain the dimensions in each layer. We used the `ELU` activation function in the first four stages of the model, which is similar to the `ReLU` activation function used in the first model. In the last stage, we used `sigmoid` activation which predicted independent probabilities. Finally, `Binary cross-entropy` was used to measure loss.
We are also using `BatchNormalization` here as a good practice to make neural networks faster and more stable through adding extra layers in a deep neural network. The new layer performs the standardizing and normalizing operations on the input of a layer coming from a previous layer. This regularization helps in preventing the over-fitting of the model and the learning process becomes more efficient.
We wanted to be able to detect multiple notes at the same time, so we omitted the `softmax` layer that is usually used for classification at the end of the CNN. This also meant that our loss function could not be a `categorical cross-entropy` function since our result would not be categorical. Instead, we used a `sigmoid` layer with a `binary cross-entropy` loss function. `Sigmoid` allows for independent probabilities, which is exactly what we wanted.

We obtained the following results on CQT pre processed data-
| Pre-Processing | Accuracy      |  Precision | Recall | F-Score |     
| -------------  | ------------- |------------|--------|---------|
| CQT            |  56.92        |   70.00    |  73.11 |  72.55  |

# POST-PROCESSING
1. We backtracked the steps of pre processing to convert the 4D Boolean matrix obtained from the Model to a 2D matrix.
2. Then we converted the 2D matrix into a 2D piano roll.
3. Using pandas, we generated the dataframe to note the start, end, pitch and velocity corresponding to each note being played.
4. Then we generated the piano roll representation for both y_pred_test.npy (obtained from the model) and the y_test.npy (original) files.
