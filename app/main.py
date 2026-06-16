from fastapi import FastAPI
import subprocess
globals = ['ping']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if any(bad_cmd in host for bad_cmd in globals):
        raise ValueError('Invalid command detected')
    subprocess.call(['ping', host])
    return {'status': 'completed'}