# move to yass home
cd /home/eduardo/dev/yass

# check commit hash, pull and checkouts
git checkout $1

# run performance test
make performance-test
