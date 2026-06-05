from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if 'localhost' in host else ''

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = generate_ping_command(host)
    if ping_command:
        subprocess.call(ping_command, shell=True)
    return {'status': 'completed'}