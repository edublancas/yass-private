# source activate yass-cpu
source activate yass

# old yass
cd ~/dev/yass
git checkout pipeline-comparison
git pull
pip install -e .
python -c 'import yass; assert yass.__version__ == "0.5dev"'
cd ~/dev/experiments

# yass nnet100k.yaml
yass nnet.yaml
mv /ssd/data/eduardo/tmp/ /ssd/data/eduardo/old-nnet

# yass threshold100k.yaml
yass threshold.yaml
mv /ssd/data/eduardo/tmp/ /ssd/data/eduardo/old-threshold

# new yass
cd ~/dev/yass
git checkout dev
git pull
pip install -e .
python -c 'import yass; assert yass.__version__ == "0.4dev"'
cd ~/dev/experiments

yass sort threshold.yaml --output_dir test-threshold/ --complete --clean

yass sort nnet.yaml --output_dir new-nnet/
yass sort threshold.yaml --output_dir new-threshold/

mv /ssd/data/eduardo/tmp/spike_train.npy /ssd/data/eduardo/spike_train.npy
