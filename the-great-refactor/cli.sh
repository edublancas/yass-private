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
pip uninstall yass-algorithm -y
pip install -e .
source activate yass
python -c 'import yass; assert yass.__version__ == "0.4dev"'
cd ~/dev/private-yass/the-great-refactor

yass sort nnet-remote.yaml --output_dir new-nnet-2/ --clean
yass sort threshold-remote.yaml --output_dir new-threshold-2/ --clean

# yass sort nnet100k.yaml --output_dir new-nnet-batch/
# yass sort threshold100k.yaml --output_dir new-threshold/