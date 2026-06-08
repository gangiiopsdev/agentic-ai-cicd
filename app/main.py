from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")

    # Use a dedicated library for ping requests instead of executing the command directly
    try:
        response = subprocess.run(['ping', '-c', '4', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'stdout': response.stdout, 'stderr': response.stderr}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stdout': e.stdout, 'stderr': e.stderr}