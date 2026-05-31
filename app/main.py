from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    try:
        # Validate input to ensure it does not contain malicious commands
        if any(char in host for char in [';', '|', '&', '$', '`']):
            raise ValueError('Invalid input')
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)