from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if 'localhost' in host else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    cmd = generate_ping_command(host)
    if cmd and not 'localhost' in host:
        subprocess.run(cmd, shell=False, check=True)
    return {'status': 'completed'}