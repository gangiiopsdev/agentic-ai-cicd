from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess with args instead of shell=True
    subprocess.call(['ping', *shlex.split(host)])
    return {'status': 'completed'}