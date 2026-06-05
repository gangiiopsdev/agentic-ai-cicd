from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}