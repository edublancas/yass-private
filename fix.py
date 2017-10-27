import matplotlib.pyplot as plt
import numpy as np

wrec = np.fromfile('wrec.bin', dtype='int16')
whiten = np.fromfile('whiten.bin', dtype='int16')

wrec.shape
whiten.shape

plt.plot(wrec[-2000:])
plt.plot(whiten[-2000:])

plt.plot(wrec)
plt.plot(whiten)


plt.plot(wrec[:1000])
plt.plot(wrec[-1000:])

plt.plot(whiten[:1000])
plt.plot(whiten[-1000:])

plt.show()

old = np.load('old.npy')
new = np.load('new.npy')

old.shape
new.shape

plt.plot(old[-100:])
plt.show()

plt.plot(new[-100:])
plt.show()


new_filtered = np.fromfile('filtered.bin').reshape((100000,7))
new_filtered.shape

old_filtered = np.fromfile('old_filrered.bin').reshape((100120,7))
old_filtered.shape

plt.plot(new_filtered[:100])
plt.plot(old_filtered[:100])
plt.show()