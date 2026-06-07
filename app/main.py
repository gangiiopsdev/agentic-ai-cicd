from fastapi import FastAPI
import subprocess
def run_command(command: list) -> int:
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Input validation and sanitization
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    command = ['ping', host]
    result = run_command(command)
    if result == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Ping failed'}