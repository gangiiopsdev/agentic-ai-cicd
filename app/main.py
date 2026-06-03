from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 50:
        return {'status': 'invalid input'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}