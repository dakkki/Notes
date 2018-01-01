'''
Optimisers:			Adam Gradient Descent
Loss function:		Cross-Entropy
Activiation:		ReLU
Neural Networks:	Feed Forward , Recurrent , Convolutional , Unsupervised (GAN)
Layers:				*Input layer:	1 layer , 1 node
					*Hidden layer:	1 - 2 layers (except for convolutional networks). The starting number of nodes can be between the number of nodes in the input later and the number of nodes in the output layer
					*Output layer:	1 layer , nodes = number of features 
'''
import numpy , random , keras , pandas , sklearn
#from sklearn import model_selection

#Import data
data = pandas.read_csv('fruits.csv')																					#Import .csv dataset
X = pandas.DataFrame.as_matrix(data[['mass' , 'width', 'height' , 'color_score']])										#Convert to numpy array
Y = pandas.DataFrame.as_matrix(data['fruit_label'])																		#Convert to numpy array
n_class = 4																												#Identify the number of classes
#Y = keras.utils.to_categorical(Y, n_class)																				#One-hot encoding. 
X , Y = sklearn.utils.shuffle(X , Y , random_state = 0)																	#Shuffle the dataset to make sure similar instances are not clustering next to each other
#train_x , test_x , train_y , test_y = model_selection.train_test_split(X , Y , random_state = 0)						#Split into train/test sets. This may not be needed because at the training function (line33) keras can automatically split the data to train and test sets

#Setup neural network
model = keras.models.Sequential()																						#Call the Sequential model object, which is a linear stack of layers
model.add(keras.layers.core.Dense(3 , input_shape = (n_class,) , activation = 'relu'))									#Hidden layer 1 with 3 nodes and the relu activation function, but here (only for the first hidden later) we must identify the shape of the input classes as (4,) because of 4 classes
#model.add(keras.layers.core.Dropout(0.02))																				#Randomly not train (not use nodes) in a network (a form of regularisation to help prevent overfitting). rate = between 0 & 1 which is the rate of dropping nodes, 0.2 = 20% of the nodes will be randomly turned off (0.2 - 0.5 is usually ideal) too low = useless, too high = underlearning. This layer can be added anywhere (before the first hidden layer, between hidden layers, etc...). It is best used on larger networks rather than small ones
model.add(keras.layers.core.Dense(3 , activation = 'relu'))																#Hidden layer 2 with 3 nodes and the relu activation function
model.add(keras.layers.core.Dense(n_class , activation = 'softmax'))													#Output layer with 4 nodes (because of 4 classes) and the softmax activation function

#Compile model
model.compile(keras.optimizers.Adam() , loss = 'sparse_categorical_crossentropy' , metrics = ['accuracy'])				#Compile the model, identify here the loss function, the optimiser, and the evaluation metric

#Train model
model.fit(X , Y , batch_size = 8 , epochs = 50 , verbose = 2 , validation_split  = 0.25)								#Preform the network training, input the training feature and class tensors, identify the batch size (conventional to use multiples of 8 - 8 , 16 , 32 etc...), and the epoch number. Verbose 23 is best to printout the epoch cycle only. The validation split is splitting the dataset into a train/test set (0.25 = 25% for the test set), thus the final accuracy we want to use is the valication accuracy (where it is measured using the test set's preformace on the model)

#Output
#score = model.evaluate(test_x , test_y , verbose = 0)																	#Use the testing feature and class tensors to evaluate the model's accuracy,not really needed since we are using the validation argument in the train function (line 33)
#print('Test accuracy:' , score[1])
'''
#Save model weights to HDF5 - sudo pip3 install h5py
model_json = model.to_json()
with open('model.json' , 'w') as json_file:
	json_file.write(model_json)
model.save_weights('model.h5')
print('Saved model to disk')
#Load model and weights
with open('model.json' , 'r') as json_file:
	json = json_file.read()
load_model = keras.models.model_from_json(json)
load_model.load_weights('model.h5')
print('Loaded model from disk')
#Evaluate loaded model
load_model.compile(keras.optimizers.Adam() , loss = 'sparse_categorical_crossentropy' , metrics = ['accuracy'])
score = load_model.evaluate(test_x , test_y , verbose = 0)
print('Test accuracy:' , score[1])
'''
#Prediction
prediction = model.predict_classes(numpy.array([[130 , 6.0 , 8.2 , 0.71]]))
print(prediction)

'''
keras.layers.Dense(units = 2 , activation = 'relu')													#All nodes connected to each other
keras.layers.Dropout(rate = 0.5)																	#Percentage of nodes to be randomly switched off during an epoch
keras.layers.Flatten()																				#Flattens a tensor into a vector (None, 64, 32, 32) ---> 64*32*32 ---> (None, 65536)
keras.layers.ZeroPadding2D(padding = (1 , 1))														#Adds rows and columns of zeros at the top, bottom, left and right side of an image tensor
keras.layers.Convolution2D(filters = 32 , kernel_size = (1 , 1) ,  activation = 'relu')				#For CNN
keras.layers.MaxPooling2D(pool_size = (2 , 2))														#Pooling the output from a CNN, it is a form of non-linear down-sampling
keras.layers.LSTM(units = 2 , activation = 'relu' , dropout = 0.25 , recurrent_dropout = 0.25)		#For RNN

'''