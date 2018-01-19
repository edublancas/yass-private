import numpy as np

st_old = np.loadtxt('old_yass_spike_train.csv', dtype=int, delimiter=',')
st = np.load('spike_train.npy')

st.shape
st_old.shape

len(np.unique(st[:, 1]))
len(np.unique(st_old[:, 1]))
