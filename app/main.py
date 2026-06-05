from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)