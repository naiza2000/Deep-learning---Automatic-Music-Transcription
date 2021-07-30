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
