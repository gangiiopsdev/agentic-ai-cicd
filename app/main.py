from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if '127.0.0.1' in host else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    command = generate_ping_command(host)
    if command:
        subprocess.run(command, shell=False, check=True)

    return {'status': 'completed'}