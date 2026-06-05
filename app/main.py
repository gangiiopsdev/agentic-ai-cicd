from fastapi import FastAPI
import subprocess
def escape_command(command):
    return ' '.join(command.split())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = escape_command(f'ping {host}')
    subprocess.call(command, shell=False)
    return {'status': 'completed'}