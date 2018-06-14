"""
https://keras.io/getting-started/sequential-model-guide/
"""

from keras.models import Sequential
from keras.layers import LSTM, Dense, Conv2D
import numpy as np


def default_model(x_train, input_shape, K1, K2):
    n_data, window_size, n_channels, _ = x_train.shape

    model = Sequential()

    model.add(Conv2D(16, kernel_size=(3, 3),
                     padding='valid', activation='relu', use_bias=True,
                     input_shape=input_shape))

    model.add(Conv2D(16, kernel_size=(3, 3),
                     padding='same', activation='relu', use_bias=True))

    model.add(Conv2D(16, kernel_size=(3, 3),
                     padding='valid', activation='relu', use_bias=True))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    return model


# model.fit(x_train, y_train,
#           batch_size=batch_size, epochs=5, shuffle=False,
#           validation_data=(x_val, y_val))