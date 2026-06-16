from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    args = ['ping', *shlex.split(shlex.quote(host))]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        execute_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}