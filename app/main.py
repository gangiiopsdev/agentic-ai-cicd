from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate the host input to ensure it only contains allowed characters
    if not host.isalnum():
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}