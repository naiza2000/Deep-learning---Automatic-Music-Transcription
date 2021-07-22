# POST PROCESSING
1. We backtracked the steps of pre processing to convert the 4D Boolean matrix obtained from the Model to a 2D matrix.
2. Then we converted the 2D matrix into a 2D piano roll.
3. Using pandas, we generated the dataframe to note the start, end, pitch and velocity corresponding to each note being played.
4. Then we generated the piano roll representation for both y_pred_test.npy (obtained from the model) and the y_test.npy (original) files. 
