from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate the host input to ensure it contains only allowed characters
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        raise ValueError('Invalid host name')
    cmd = 'ping {}
    result = subprocess.run(shlex.split(cmd), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}