from fastapi import FastAPI
import subprocess
import shlex
global safe_ping, app

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to prevent injection
    if not all(c.isalnum() for c in host) or len(host.split('.')) != 4:
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}