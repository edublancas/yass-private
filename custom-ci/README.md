# custom CI

Simple CI service to automatically test our codebase in
custom hardware.

## Instructions

Install requirements first:

```shell
# redis
sudo apt install redis-server

# python packages
pip install -r requirements.txt
```

## Starting services

```shell
# run redis
redis-server --daemonize yes

# start rq
nohup rq worker  --url redis://localhost:6379 performance-testing& &> /dev/null

# start flask app
gunicorn app:app --bind 0.0.0.0:5000 --daemon
```

## References

* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs