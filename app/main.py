from fastapi import FastAPI
import subprocess
import shlex

global_args = shlex.split('ping')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = global_args + [host]
    subprocess.call(args)
    return {'status': 'completed'}