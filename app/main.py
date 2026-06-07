from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    execute_ping(host)
    return {'status': 'completed'}