import mmap

f = open('ej49_data1_set1.bin', 'r+b')

x = mmap.mmap(f.fileno(), 0)


%%timeit
x[:100]


%%timeit
x[10:70:1]


%%timeit
x[10:70:10]


f.close()