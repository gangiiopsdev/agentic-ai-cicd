from fastapi import FastAPI
import subprocess
global timeout = 10

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with a timeout and avoiding shell=True
    args = ['ping', '-c', str(timeout), host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}