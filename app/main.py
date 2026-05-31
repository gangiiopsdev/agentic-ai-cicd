from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError("Invalid host")
    # Use shlex to safely handle shell commands
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}