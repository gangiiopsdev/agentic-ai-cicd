from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    if subprocess.call(args) != 0:
        raise Exception('Ping failed')
    return {'status': 'completed'}