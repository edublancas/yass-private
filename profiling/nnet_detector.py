"""
Profiling neural network detector
"""
from yass.neuralnetwork import NeuralNetDetector, NeuralNetTriage, nn_detection
import yass

yass.set_config('nnet-remote.yaml')
CONFIG = yass.read_config()


nnd = NeuralNetDetector(CONFIG.neural_network_detector.filename,
                        CONFIG.neural_network_autoencoder.filename)
nnt = NeuralNetTriage(CONFIG.neural_network_triage.filename)


neighbors = CONFIG.neighChannels,
geom = CONFIG.geom,
temporal_features = CONFIG.spikes.temporal_features,
temporal_window = 3,
th_detect = CONFIG.neural_network_detector.threshold_spike,
th_triage = CONFIG.neural_network_triage.threshold_collision,
detector_filename = CONFIG.neural_network_detector.filename,
autoencoder_filename = CONFIG.neural_network_autoencoder.filename,
triage_filename = CONFIG.neural_network_triage.filename
