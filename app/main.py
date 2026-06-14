from fastapi import FastAPI
import subprocess
import shlex

global_config = {'ping_command': 'ping'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex to safely split the command string
    command = [global_config['ping_command'], *shlex.split(host)]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}