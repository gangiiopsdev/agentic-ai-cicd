from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shell=False and executable=None to avoid command injection
    subprocess.call(['ping', host], shell=False, executable=None)
    return {'status': 'completed'}