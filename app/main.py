from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    if '||' in args or '&' in args:
        raise ValueError('Invalid command argument')
    subprocess.call(args)

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_fixed(host: str):
    # Fixed implementation
    args = ['ping', host]
    if '||' in args or '&' in args:
        raise ValueError('Invalid command argument')
    subprocess.call(args)
    return {'status': 'completed'}