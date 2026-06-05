from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Sanitize the host parameter to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid hostname'
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}