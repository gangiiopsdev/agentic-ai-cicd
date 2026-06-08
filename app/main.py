from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[0-9.]+$', host) or '.' not in host:
        raise ValueError('Invalid host format')
    try:
        command = ['ping', '-c', '4'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'''

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}