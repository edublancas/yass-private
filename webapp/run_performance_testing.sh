# start yass env
source activate yass

# move to yass home
cd /home/eduardo/dev/yass-copy

# check commit hash, pull and checkouts
git checkout $1
git pull

# run performance test
make performance-test
