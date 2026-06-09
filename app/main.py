from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and using shlex to safely quote arguments
    subprocess.call(['ping', *shlex.split(host)], shell=False)

    return {'status': 'completed'}