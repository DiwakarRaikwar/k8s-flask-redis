from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis-service')
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def index():
    count = r.incr('hits')
    return f'''
    <h1>🚀 Flask + Redis on Kubernetes</h1>
    <p>This page has been visited <b>{count}</b> times.</p>
    <p>Built by: Diwakar Raikwar</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)