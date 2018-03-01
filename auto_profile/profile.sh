cd ~/dev/yass
git checkout master
git pull
pip install -e .
cd ~/dev/private-yass/auto_profile
mprof run 49.py