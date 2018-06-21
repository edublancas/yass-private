# start redis
screen -S redis
redis-server

# start rq (inside webapp folder)
screen -S rq
rq worker  --url redis://localhost:6379 performance-testing

# flask
screen -S flask
export FLASK_APP=app.py
flask run --host=0.0.0.0