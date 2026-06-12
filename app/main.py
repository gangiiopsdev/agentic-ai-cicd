from fastapi import FastAPI
import subprocess
import shlex
global ping_command
ping_command = 'ping {}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    command = shlex.split(ping_command.format(host))
    subprocess.run(command, check=True)

    return {'status': 'completed'}