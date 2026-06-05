from fastapi import FastAPI
import re
import shlex
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)