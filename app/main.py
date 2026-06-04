from fastapi import FastAPI
import subprocess
import shlex
global_args = {"host": "8.8.8.8"}
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str = None):
    if not host:
        host = global_args['host']
    cmd_parts = ['ping', shlex.quote(host)]
    subprocess.run(cmd_parts, check=True)
    return {'status': 'completed'}