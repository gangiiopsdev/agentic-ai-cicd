from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = 'ping'
    args = [command] + shlex.split(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}