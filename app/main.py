from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping -c 1 {shlex.quote(host)}'
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(generate_ping_command(host), shell=False, check=True)
    return {'status': 'completed'}