from fastapi import FastAPI
import subprocess
good_subprocesses = ['ping']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in good_subprocesses:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid command')
    return {'status': 'completed'}