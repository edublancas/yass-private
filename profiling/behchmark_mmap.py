import numpy as np

shape = (10000, 10000)
x = np.random.rand(*shape)
x.tofile('data.bin')
del x


class MemoryMap(np.memmap):
    """Subclass of numpy.memmap that returns np.ndarray when indexing
    """
    def __getitem__(self, index):
        res = super(MemoryMap, self).__getitem__(index)
        return np.array(res)

m = np.memmap('data.bin', dtype='float64', shape=shape, mode='r')

m_ = MemoryMap('data.bin', dtype='float64', shape=shape, mode='r')

j = m[:, :]

j____ = m_[:, :]

m__ = np.array(m[:, :])

x = m_ + 1

%%timeit
m[:, 0] + 1

q
a = np.array(m[:, 0])

%%timeit
a + 1


s = m[:, 0]
type(s)

s + 1

del m
del s
