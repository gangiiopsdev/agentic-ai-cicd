from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    if 'localhost' in host or '127.0.0.1' in host:
        return f'ping {host}'
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    if command:
        subprocess.run(command, shell=False, check=True)
    return {'status': 'completed'}