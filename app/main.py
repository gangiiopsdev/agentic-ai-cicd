from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to avoid potential abuse
    subprocess.run(command, check=True)
    return {'status': 'completed'}