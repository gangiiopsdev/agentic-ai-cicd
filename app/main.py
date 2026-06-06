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
    # Secure implementation
    command = generate_ping_command(host)
    args = command.split(' ')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}