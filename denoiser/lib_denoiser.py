import numpy as np
from yass.templates import TemplatesProcessor
from yass.templates import util as templates_util

class SpikeIndex:
    """Wraps spike index logic
    """
    
    def __init__(self, spike_index_array, channel_index=None, geometry=None,
                 neighbors=None):
        self.arr = spike_index_array
        self.channel_index = channel_index
        self.geometry = geometry
        self.neighbors = neighbors
       
    def get_spike_index_for_channel(self, channel):
        sub = self.arr[self.arr[:, 1] == channel]
        return SpikeIndex(sub, self.channel_index, self.geometry,
                            self.neighbors)
    
    def get_times_from_channel(self, channel, max_ptp=None, rec=None,
                               waveform_length=51):
        if max_ptp is None:
            return self.arr[self.arr[:, 1] == channel][:, 0]
        else:
            times = self.arr[self.arr[:, 1] == channel][:, 0]
            spikes = read_waveforms(rec, times, waveform_length,
                                    random_shift=False,
                                    add_offset=True)
            ptps = templates_util.ptps(spikes)
            return times[ptps <= max_ptp]
    
    def get_times(self):
        return self.arr[:, 0]
    
    @property
    def shape(self):
        return self.arr.shape
    
    @property
    def n_unique_channels(self):
        return len(np.unique(self.arr[:, 1]))
    
    def count_spikes_per_channel(self):
        chs, counts = np.unique(self.arr[:, 1], return_counts=True)
        return {ch: count for ch, count in zip(chs, counts)}
    
    def read_waveforms_from_channel(self, rec, channel, waveform_length=51,
                                    random_shift=False,
                                    only_neighbors=True):
        """Read waveforms from rec using an array of spike times
        """
        n_obs, n_channels = rec.shape
    
        if channel is not None:
            idxs = self.get_times_from_channel(channel)
#             print(idxs, idxs.shape)
        else:
            idxs = self.get_times()
#             print(idxs, idxs.shape)
    
        out = np.empty((len(idxs), waveform_length, 7 if only_neighbors else n_channels))
        half = int((waveform_length - 1)/2)
    
        for i, idx in enumerate(idxs):
        
            if random_shift:
                offset = np.random.randint(-half, half)
            else:
                offset = 0

            if only_neighbors:
                out[i, :] = rec[idx-half + offset:idx+half+1 + offset, self.channel_index[channel]]
            else:
                out[i, :] = rec[idx-half + offset:idx+half+1 + offset]

        return out
 

# FIXME: remove duplicated logic
def read_waveforms(rec, times, waveform_length, random_shift=False, add_offset=False):    
    """Read waveforms from rec using an array of spike times
    """
    n_obs, n_channels = rec.shape

    out = np.empty((len(times), waveform_length, n_channels))
    valid_time = np.ones(len(times))

    half = int((waveform_length - 1)/2)

    for i, time in enumerate(times):
        if add_offset:
            offset = -20
        else:
            offset = 0
    
        if random_shift:
            offset += np.random.randint(-3, 3)
        
        s = slice(time - half + offset, time + half + 1 + offset)
    
        if s.start >= 0 and s.stop <= n_obs:
            out[i] = rec[s]
        else:
            valid_time[i] = 0
            print('invalid time')

    return out[valid_time.astype(bool)]