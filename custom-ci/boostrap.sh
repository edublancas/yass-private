sudo apt install redis-server

# start redis
redis-server

# start rq
rq worker  --url redis://localhost:6379 performance-testing