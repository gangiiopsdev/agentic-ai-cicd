from fastapi import FastAPI
import subprocess
import shlex
global subprocess_count
subprocess_count = 0

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global subprocess_count
    if subprocess_count < 5:
        try:
            subprocess.call(shlex.split(f'ping {host}'))
            subprocess_count += 1
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'status': 'Too many ping requests'}
    return {'status': 'completed'}