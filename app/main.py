from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.split to safely handle user input
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}