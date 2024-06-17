import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from keras.callbacks import EarlyStopping
# Import `Sequential` from `keras.models`
from keras.models import Sequential

# Import `Dense` from `keras.layers`
from keras.layers import Dense

df = pd.read_csv("dataset\heart.csv")


X = df.iloc[:, 0:13]
y = df.iloc[:, 13:14]

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
early_stopping = EarlyStopping(monitor='val_accuracy', patience=350)  # Monitor validation accuracy, stop after 5 epochs with no improvement

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  # Adjust loss and optimizer as needed

# Train the model with EarlyStopping
model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test), callbacks=[early_stopping])



# Training Model
#model.fit(X_train, y_train, epochs = 500,
           #batch_size = 1, verbose = 1)

# Predicting the Value

X_ans1 = df.iloc[199:202, 13:14]


X_test = df.iloc[199:202, 0:13]

y_pred = model.predict(X_test)
print(f'answer = {X_ans1}')
print(f'X_test = {X_test}')
print(f'predict = {y_pred}')

model.save('my_model.h5')


