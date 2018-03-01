from yass.batch import BinaryReader
import numpy as np

shape = 10, 100
data = np.array(np.arange(1000)).reshape(shape).astype('int32')

data.tofile('data_C.bin')
data.T.tofile('data_F.bin')

data

with open('data_C.bin', 'rb') as f:
    print(np.frombuffer(f.read(4*100), 'int32'))


with open('data_F.bin', 'rb') as f:
    print(np.frombuffer(f.read(4*100), 'int32'))


c = BinaryReader('data_C.bin', 'int32', shape, 'C')
f = BinaryReader('data_F.bin', 'int32', shape, 'F')


data
data[5:10, 5:12]
c[5:10, 5:12]
f[5:10, 5:12]

np.testing.assert_equal(data[5:10, 5:12], c[5:10, 5:12])
np.testing.assert_equal(data[5:10, 5:12], f[5:10, 5:12])

data[1:10, 2:3]
f[1:10, 2:3]
c[1:10, 2:3]

np.testing.assert_equal(data[1:10, 2:3], c[1:10, 2:3])
np.testing.assert_equal(data[1:10, 2:3], f[1:10, 2:3])


data[:10, :3]
f[:10, :3]
c[:10, :3]

np.testing.assert_equal(data[:10, :3], c[:10, :3])
np.testing.assert_equal(data[:10, :3], f[:10, :3])

data[3:, 95:]
f[3:, 95:]
c[3:, 95:]

np.testing.assert_equal(data[3:, 95:], c[3:, 95:])
np.testing.assert_equal(data[3:, 95:], f[3:, 95:])

c[:]
c[:, :, :]
c[::1, :]
c[:, ::1]



map_wide = np.memmap('data_C.bin', 'int32', shape=(100, 100000)).T
map_long = np.memmap('data_F.bin', 'int32', shape=(100000, 100))

%%timeit
wide[1000:2000, 5:8]

%%timeit
map_wide[1000:2000, 5:8]


%%timeit
long[1000:2000, 5:8]

%%timeit
map_long[1000:2000, 5:8]
