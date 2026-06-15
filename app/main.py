from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}