source activate yass-cpu
cd ~/dev/yass
git checkout reader
git pull
pip install -e .
cd ~/dev/private-yass/auto_profile
mprof run 49.py