# MODEL:

In the first model we implemented a `Recurrent Neural Network` (RNN) using `Long Short Term Memory` (LSTM) architecture to capture temporal dependancies of audio data.<br/>
We used `three` LSTM layers and one `Dense` layer. The input shape of the model is `[batch, time frames, features]` Batch size was set to `100`. `tanh` activation was used in the LSTM Layers and `sigmoid` was used in the outer layer. After each LSTM layer, a dropout of `20%` was used to minimise overfitting. Each LSTM layer gave `256` dimensional output for each time frame and the outer layer gave `88` dimensional output which corresponds to the 88 keys on a piano. We used a learning rate of `0.01` and trained the model over `50` epochs. Loss was calculated using `binary_crossentropy` and `adam` optimizer was used. Since sigmoid function gives a real value between 0 and 1, we used a threshold of `0.5` to predict whether the note is played or not. Therefore, the final output is a boolean matrix with zeros and ones.



# Training on dataset processed using STFT






# Training on dataset processed using Mel-spectrogram






# Training on dataset processed using CQT - Transform




