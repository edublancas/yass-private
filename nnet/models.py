"""
https://keras.io/getting-started/sequential-model-guide/
"""

from keras.models import Sequential
from keras.layers import LSTM, Dense, Conv2D, Flatten

def default_model(x_train, input_shape):
    n_data, window_size, n_channels, _ = x_train.shape

    model = Sequential()

    model.add(Conv2D(32, kernel_size=(window_size, 1),
                     padding='valid', activation='relu', use_bias=True,
                     input_shape=input_shape, data_format="channels_last"))

    model.add(Conv2D(32, kernel_size=(1, 1),
                     padding='same', activation='relu', use_bias=True,
                     data_format="channels_last"))

    model.add(Conv2D(1, kernel_size=(1, n_channels),
                     padding='valid', activation='linear', use_bias=True,
                     data_format="channels_last"))
    
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    
    model.summary()

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    return model
