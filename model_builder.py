import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Import sklearn for split data
from sklearn.model_selection import train_test_split
# Import EarlyStopping for early stopping technic
from keras.callbacks import EarlyStopping
# Import `Sequential` from `keras.models` for create Sequential model
from keras.models import Sequential
# Import `Dense` from `keras.layers` for create layer
from keras.layers import Dense

# Import data
df = pd.read_csv("dataset\heart.csv")

# Choose columns for independent(X) and dependent(y) 
X = df.iloc[:, 0:13]
y = df.iloc[:, 13:14]
# Split data to train and test for X and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15)

# Initialize the constructor
model = Sequential()

# Add an input layer
model.add(Dense(13, activation ='relu', input_shape =(13, )))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add one hidden layer
model.add(Dense(12, activation ='relu'))

# Add an output layer
model.add(Dense(1, activation ='sigmoid'))

# Model output shape
model.output_shape

# Model summary
model.summary()

# Model config
model.get_config()

# List all weight tensors
model.get_weights()
model.compile(loss ='binary_crossentropy', 
optimizer ='adam', metrics =['accuracy'])


# Define the EarlyStopping callback
early_stopping = EarlyStopping(monitor='val_accuracy', patience=350)  # Monitor validation accuracy, stop after 350 epochs with no improvement

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  # Adjust loss and optimizer as needed

# Train the model with EarlyStopping
model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test), callbacks=[early_stopping])

# Predicting the Value
y_pred = model.predict(X_test)

#Save model .h5 for using in Flask
model.save('my_model.h5')


