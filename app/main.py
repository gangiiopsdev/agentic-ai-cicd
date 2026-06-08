from fastapi import FastAPI
import subprocess
global ping_command
ping_command = 'ping {}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(ping_command.format(host), shell=True)
    return {'status': 'completed'}