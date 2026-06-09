from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host and 'ping' in host:
        return None
    return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = safe_ping(host)
    if command:
        args = [command]  # Use a list to avoid shell=True
        subprocess.run(args, check=True)
    return {'status': 'completed'}