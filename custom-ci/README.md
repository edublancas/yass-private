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

# start rq from custom-ci folder
cd PATH/TO/CUSTOM-CI
nohup rq worker  --url redis://localhost:6379 performance-testing& &> /dev/null

# start flask app
gunicorn app:app --bind 0.0.0.0:5000 --daemon
```

## Sending tasks

By making a request to the server: `IP:PORT/yass/[git_hash]`

Or direcly using Python

```python
"""
Example for sending a task to the Queue
"""
from redis import Redis
import rq

queue = rq.Queue('performance-testing',
                 connection=Redis.from_url('redis://localhost:6379'),
                 default_timeout=3600)

job = queue.enqueue('tasks.performance_testing', 'testing')

job.get_id()
```

## References

* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs