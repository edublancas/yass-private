import os
import numpy as np

from yass import geometry

root = '/Users/Edu/data/yass'

path_to_geom = os.path.join(root, 'ej49_geometry1.txt')

n_channels = 49

geom = geometry.parse(path_to_geom, n_channels)
neighbors = geometry.find_channel_neighbors(geom, radius=70)
steps = geometry.n_steps_neigh_channels(neighbors, steps=2)
groups = geometry.make_channel_groups(n_channels, neighbors, geom)

groups

# get neighbors for some channel
np.where(neighbors[10])

geometry.order_channels_by_distance(1, np.array([5, 6, 7]), geom)


max_neighbors = np.max(np.sum(neighbors, axis=0))
c_idx = np.ones((n_channels, max_neighbors), 'int32') * n_channels

for c in range(n_channels):
    ch_idx, _ = geometry.order_channels_by_distance(c,
                                                    np.where(neighbors[c])[0],
                                                    geom)
    c_idx[c, :ch_idx.shape[0]] = ch_idx

c_idx
