# Deep-learning---Automatic-Music-Transcription
This repository contains the research done and the codes written for the semester project - Automatic Music Transcription, offered by Electronics Club IIT Kanpur, and mentored by me.   
1. We have explored various models, for example, CNN, RNN and models with the combination of two, with a sole motive of achieveing maximum accuracy. 
2. For preprocessing of the music files, we have tried various ways, for example, `constant Q- transform`, `Short- time fourier transform`, and `mel-frequency cepstrum`, and have compared the results with respect to the model used. 
3. Each folder in this repository represents a different model trained for automatic music transcription. 
4. We will keep on updating the repository until we arrive at the end dates of the projects.  

Till then, stay tuned. 

Preprocessing of .wav and .mid files:

To extract information about frequency, time and amplitude from a given audio files, we have converted them to spectrograms by employing the use of:
  1. Constant Q Transform - For a span of 7 octaves with 36 frequency bins each, the total number of frequency bins taken was 252. We chose a sample rate of 16000 and a 'hop length' of 512 (Powers of 2 are generally used)
  2. Short-Time Fourier Transform - For maximum frequency resolution with STFT, window size should be taken as the entire span of the file. However, this is accompanied by very low time resolution (uncertainty principle for the Fourier Transform). Therefore, to ensure reasonable resolution for both frequency as well as time, our project uses 2048 as window size (and 512 as hop length).
  3. Mel-Frequency Cepstrum - The human ear perceives frequencies logarithmically. Although time-frequency relation and a relevant representation of amplitude are taken care of in using STFT and CQT, MFCCs provide perceptually-relevant frequency representation as well. Even though higher order coefficients in MFCCs represent increasing levels of spectral details, depending on the sampling rate and estimation method, 12 to 20 cepstral coefficients are optimal for typical models. We have used 13 coefficients.

Mel Spectrograms are especially useful when it comes to extracting information regarding different instruments or timbre. Since our models deal only with piano music, all the aforementioned methods work well. 

For the RNN models, input was required in the form of a 3D array. The .wav files with n rows (in array form) such that n = (100 * p) + q, are converted to 3D-arrays of dimensions (p, 100, 252) and concatenated. The .mid files are converted to piano roll form with similar arrays and padded to ensure uniformity in shape of output from model and available piano roll. The difference between these two will provide the error/loss for the model.

RNN Preprocessing using Mel Transform: https://colab.research.google.com/drive/1teTNEOXTV9DUJa67dNzluMtjqs7yKtAn?usp=sharing
