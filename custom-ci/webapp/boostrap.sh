# start redis
redis-server

# start rq (inside webapp folder)
rq worker  --url redis://localhost:6379 performance-testing