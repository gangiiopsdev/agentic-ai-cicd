from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {'status': 'completed'}