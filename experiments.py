raw = np.fromfile(path, dtype='int16').reshape(obs_total, n_channels)

res = butterworth(raw, low_freq=300, high_factor=0.1, order=3, sampling_freq=20000)


b = np.fromfile('../tests/butterworth.bin', dtype=dtype).reshape(obs_total, n_channels)

res[-4:, :2] ==b[-4:, :2]

res[~np.isclose(res, b)]
b[~np.isclose(res, b)]

import matplotlib.pyplot as plt

plt.plot(b)
plt.show()