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