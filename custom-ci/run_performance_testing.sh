# Run performance testing

# start yass env
source activate yass

# move to yass home
cd /home/eduardo/dev/yass

# check commit hash, pull and checkouts
git checkout $1
git pull
git --no-pager show --oneline -s

# run performance test
make performance-test
