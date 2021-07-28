
# PREPROCESSING:
`1. Short Time Fourier Transform`

The Fourier transform of an audio signal tells which frequencies are present in the signal along with the intensity of that frequency. 
If it is applied over the full audio signal, it loses the information of time dependence of these frequencies (that is when they occur). 
More precisely, Fourier Transform of a signal gives all the frequencies appearing in the signal averaged out over the duration (on which the transform is applied).

Hence, the Fourier transform is applied on different segments of signal one by one, and then all the outputs are then stitched together providing a more rigorous analysis.

There is a possible chance of generating unwanted frequency values due to the signal present at the ends of each 'window' considered. 
Hence the signal is smoothened out at the ends (the magnitude is lowered by applying a weight) for reducing any error.
Consequently, a window generally overlaps its previous window so that the information present in the signal at the ends of a window is counted again and preserved at its best.

The number of samples in each window taken is 512.

The hop size of each window is 256.

The number of samples in each window taken is in the power of 2. It greatly reduces the time complexity in the Fast Fourier transform algorithm.


`2. Constant Q Transforms`

CQT transform varies frequencies on a logarithmic scale whereas STFT varies it linearly.
Also, CQT shows more accuracy for lower frequencies bins and comparatively lesser for higher frequencies bins as the signal is effectively covered in the lower range.

As frequency is varied exponentially on the axis, the distance between the harmonics is nearly constant
whereas in the STFT the distance between harmonics varies exponentially.

CQT has an edge over STFT when several octaves are present substantially in the audio signal.


`3. Mel Spectograms`

Mel Spectograms are a plot against the Mel scale vs time (rather than the frequency vs time).
One differentiates between frequencies in terms of how he perceives its pitch.
As frequency and pitch vary exponentially, the same difference between any 2 frequencies will not correspond to same perceptual difference in their pitch at all values.

In the Mel scale, the same difference between any 2 Mels correspond to perceptually similar difference in the pitch. 
Therefore signal is analyzed in another scale, Mel scale.
This is done by applying a Mel filter to the output of our original STFT.

The number of samples in each window taken is 2048.

The hop size of each window is 512.

Number of Mel bands taken = 252.

# MODEL

In the first model we implemented a convolutional neural network (CNN) using tensorflow.
We built a sequential model which consists of 5 stages in total. The first two stages comprise of the `Conv2D layers` and the last three consist of `Dense layers`. The input shape for the model is `(None, 100, 1, 252)` which corresponds to `(Batch No, height, depth, width)`. After each Conv2D layer and dense layers, `batch normalisation` was added to standardise and normalise the operations on the input of a layer coming from a previous layer. 
A `dropout` layer was added after each batch normalisation layer. The number inside each dropout layer represents the fraction of activations or intermediate data nodes dropped which helps prevent overfitting of the model. 
We added a `Max Pooling layer` in the second stage to reduce the width dimension from `1000` to `200`. In each dense layer added, the number inside corresponds to how many neurons are present in the layer. We used the `ReLU` activation function in the first 4 stages instead of tanh or sigmoid because the ReLU function does not saturate easily, unlike the sigmoid and tanh functions. However in the last stage we used `sigmoid` function since we had to predict an output with values between 0 and 1 only. 
Finally, `Binary cross-entropy` was used as the loss function to measure loss between the predicted and ground truth vectors with multiple active labels.

In order to convert the output matrix to a Boolean matrix, we determined the `threshold` by having our model predict note probabilities over the validation data inputs and comparing the predictions of the system to the ground truth or binary vectors. We find this threshold by calculating the `precision-recall-curve` for potential thresholds across all notes. We then use the same threshold for evaluation over testing data. 



# POST PROCESSING
1. We backtracked the steps of pre processing to convert the 4D Boolean matrix obtained from the Model to a 2D matrix.
2. Then we converted the 2D matrix into a 2D piano roll.
3. Using pandas, we generated the dataframe to note the start, end, pitch and velocity corresponding to each note being played.
4. Then we generated the piano roll representation for both y_pred_test.npy (obtained from the model) and the y_test.npy (original) files.
