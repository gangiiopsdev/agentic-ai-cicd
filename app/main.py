from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}