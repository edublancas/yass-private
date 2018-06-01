from redis import Redis
import rq
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.redis = Redis.from_url('redis://localhost:6379')
    app.task_queue = rq.Queue('performance-testing', connection=app.redis,
                              default_timeout=3600)
    return app


app = create_app()


@app.route('/yass/<git_hash>')
def hello_world(git_hash):
    job = app.task_queue.enqueue('tasks.performance_testing', git_hash)
    return 'Testing yass@{}, job with id {}'.format(git_hash, job.get_id())
