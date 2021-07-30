
In this model we implemented a `Deep Neural Network`.<br/>
We concatenated all the spectrograms to get the input array. Likewise, all the piano-rolls are joined to get the output array. In this method, the model will not be able to learn time dependance of audio data. We used `three` inner layers and one outer layer. Batch size was set to `512`. `relu` activation was used in the first two Layers and `sigmoid` was used in the outer layer. In the third layer, we did not use `relu` because it does not give negative outputs and hence sigmoid will only be able give outputs greater than 0.5. Hence, we used `tanh` in the third layer.  After each inner layer, a dropout of `30%` was used to minimise overfitting. The first two inner layers gave `256` dimensional output for each time frame, while the third layer gave `128` dimensional output. The outer layer gave `88` dimensional output which corresponds to the 88 keys on a piano. We trained the model over `50` epochs. Loss was calculated using `binary_crossentropy` and `adam` optimizer was used. We used `Early Stopping` to prevent overfitting the train data. Since sigmoid function gives a real value between 0 and 1, we used a threshold of `0.5` to predict whether the note is played or not. Therefore, the final output is a boolean matrix with zeros and ones.
<br/>
<br/>
The results of training are in the following table : 
|        Preprocessing        |No. of features|Accuracy|Precision|  Recall  |F-Score|  Loss  |
|  ---                        |     ---       |  ---   | ---     |   ---    |   --- |  ---   |
| CQT-Transform               |      252      |   .49  |   .75   |    .59   |  .66  |  .1017 |


![alt text](https://github.com/agarwalapurb/Deep-learning---Automatic-Music-Transcription/blob/main/MODEL%20-%20(DNN)/dnn_actual.PNG)

![alt text](https://github.com/agarwalapurb/Deep-learning---Automatic-Music-Transcription/blob/main/MODEL%20-%20(DNN)/dnn_predicted.PNG)
