from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using os.system instead of shell=True
    safe_command = f'ping {host}'
    subprocess.call(safe_command, shell=False)
    return {'status': 'completed'}