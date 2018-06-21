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
