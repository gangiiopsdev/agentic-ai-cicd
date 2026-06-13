from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Validate input more strictly to prevent command injection
    if not re.match('^[a-zA-Z0-9-.]+$', host):
        return {'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not re.match('^[a-zA-Z0-9-.]+$', host):
        return {'error': 'Invalid input'}
    return safe_ping(host)