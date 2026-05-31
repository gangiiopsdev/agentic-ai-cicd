from fastapi import FastAPI
import subprocess
global_args = ['ping', '--']
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = global_args + [host]
    subprocess.call(args)
    return {'status': 'completed'}