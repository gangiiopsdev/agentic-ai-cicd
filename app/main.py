from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}