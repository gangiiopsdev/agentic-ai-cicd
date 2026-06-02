from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}