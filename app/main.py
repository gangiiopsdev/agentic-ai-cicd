from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or len(host) > 15:
        return {'status': 'invalid input'}
    subprocess.call(['ping', subprocess.list2cmdline([host])])
    return {'status': 'completed'}