from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> dict:
    # Safe implementation with validation and quoting
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)