from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using shlex.split for argument splitting
    ping_command = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(ping_command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters
    if any(char in host for char in [";', '&', '$', '|', '"", '<', '>', '(`)']):
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)