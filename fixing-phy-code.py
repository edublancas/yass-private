import yass
import numpy as np

spike_train = np.load('spike_train.npy')
templates = np.load('templates.npy')

yass.set_config('config.yaml')
CONFIG = yass.read_config()
