from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command_parts):
    try:
        output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timed out'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    command_parts = ['ping', '-c', '1'] + shlex.split(host)
    return execute_command(command_parts)