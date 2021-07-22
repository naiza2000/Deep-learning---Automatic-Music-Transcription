# MODEL

In the first model we implemented a convolutional neural network (CNN) using tensorflow.
We built a sequential model which consists of 5 stages in total. The first two stages comprise of the `Conv2D layers` and the last three consist of `Dense layers`. The input shape for the model is `(None, 38, 1, 252)` which corresponds to `(Batch No, height, depth, width)`. After each Conv2D layer and dense layers, `batch normalisation` was added to standardise and normalise the operations on the input of a layer coming from a previous layer. 
A `dropout` layer was added after each batch normalisation layer. The number inside each dropout layer represents the fraction of activations or intermediate data nodes dropped which helps prevent overfitting of the model. 
We added a `Max Pooling layer` in the second stage to reduce the width dimension from `1000` to `200`. In each dense layer added, the number inside corresponds to how many neurons are present in the layer. We used the `ReLU` activation function in the first 4 stages instead of tanh or sigmoid because the ReLU function does not saturate easily, unlike the sigmoid and tanh functions. However in the last stage we used `sigmoid` function since we had to predict an output with values between 0 and 1 only. 
Finally, `Binary cross-entropy` was used as the loss function to measure loss between the predicted and ground truth vectors with multiple active labels.

In order to convert the output matrix to a Boolean matrix, we determined the `threshold` by having our model predict note probabilities over the validation data inputs and comparing the predictions of the system to the ground truth or binary vectors. We find this threshold by calculating the `precision-recall-curve` for potential thresholds across all notes. We then use the same threshold for evaluation over testing data. 



# POST PROCESSING
1. We backtracked the steps of pre processing to convert the 4D Boolean matrix obtained from the Model to a 2D matrix.
2. Then we converted the 2D matrix into a 2D piano roll.
3. Using pandas, we generated the dataframe to note the start, end, pitch and velocity corresponding to each note being played.
4. Then we generated the piano roll representation for both y_pred_test.npy (obtained from the model) and the y_test.npy (original) files. 
