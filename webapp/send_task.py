from redis import Redis
import rq

queue = rq.Queue('performance-testing',
                 connection=Redis.from_url('redis://localhost:6379'))

job = queue.enqueue('tasks.performance_testing', 'testing')

job.get_id()
