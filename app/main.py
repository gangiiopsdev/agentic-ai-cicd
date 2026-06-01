from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run and shlex.quote to avoid shell=True and command injection
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not os.path.basename(host) == host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)