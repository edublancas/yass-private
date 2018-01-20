# source activate yass-cpu
source activate yass

# old yass
cd ~/dev/yass
git checkout pipeline-comparison
git pull
pip install -e .
python -c 'import yass; assert yass.__version__ == "0.5dev"'
cd ~/dev/experiments
# yass nnet.yaml
yass threshold.yaml

mv /ssd/data/eduardo/spike_train.csv /ssd/data/eduardo/old_yass_spike_train.csv

# new yass
cd ~/dev/yass
git checkout dev
git pull
pip install -e .
python -c 'import yass; assert yass.__version__ == "0.4dev"'
cd ~/dev/experiments
# yass sort nnet.yaml
yass sort threshold.yaml

mv /ssd/data/eduardo/tmp/spike_train.npy /ssd/data/eduardo/spike_train.npy