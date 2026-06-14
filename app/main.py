from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and capture_output=True
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}