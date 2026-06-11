from fastapi import FastAPI
import re
import subprocess
def safe_ping(host):
    # Validate user input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]+$', host) or len(host) > 255:
        return False
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_subprocess(command):
    # Validate and sanitize command arguments to prevent injection
    if not all(arg.isalnum() for arg in command[1:]) or len(command) < 2:
        return False
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    if isinstance(output, bool) and not output:
        return {'status': 'failed', 'error': 'Invalid input'}
    else:
        return {'status': 'completed', 'output': output}

@app.get('/command')
def run_command(command: str):
    output = safe_subprocess(['ping', '-c', '1', command])
    if isinstance(output, bool) and not output:
        return {'status': 'failed', 'error': 'Invalid input'}
    else:
        return {'status': 'completed', 'output': output}