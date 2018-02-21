
big_data_wide = np.array(np.arange(10000000)).reshape(100, 100000).astype('int32')
big_data_wide.tofile('big_data_wide.bin')
big_data_long = big_data_wide.T
big_data_long.tofile('big_data_long.bin')

wide = BinaryReader('big_data_wide.bin', 'int64', 10, 'wide')
map_wide = np.memmap('big_data_wide.bin', 'int64', shape=(10, 1000)).T

%%timeit
wide[1000:2000, 5:8]

%%timeit
map_wide[1000:2000, 5:8]


long = BinaryReader('data_long.bin', 'int64', 10, 'long')
map_long = np.memmap('data_long.bin', 'int64', shape=(1000, 10))

%%timeit
long[1000:2000, 5:8]

%%timeit
map_long[1000:2000, 5:8]
