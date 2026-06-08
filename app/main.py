from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Simple regex to allow alphanumeric characters and some special characters
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

git_path = 'git'  # Assuming this is a predefined safe command

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run([git_path, host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}