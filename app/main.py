from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation and quoting
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)