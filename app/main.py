from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and some special characters
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid input"}
    # Use subprocess.run instead of subprocess.call
    command = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}