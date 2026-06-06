from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid host")
    return ping(host)