from fastapi import FastAPI
import subprocess
c import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}