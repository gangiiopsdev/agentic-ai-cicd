from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation using shlex to safely handle shell arguments
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}