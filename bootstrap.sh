"""
Install from scratch
"""

# create test env
conda create --name test -y
source activate test

# install last stable version
pip install yass-algorithm

# clone repo to get the sample data
git clone https://github.com/paninski-lab/yass

# move to the examples folder and run yass in the sample data
cd yass/examples
yass config_sample.yaml

# see the spike train
cat data/spike_train.csv

# remove test env
conda env remove --name test -y

# remove tmp repo
