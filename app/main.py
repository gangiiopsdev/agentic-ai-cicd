from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Use subprocess.run with shell=False and list arguments to avoid injection attacks
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)