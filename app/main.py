from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')
def safe_ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid host name')
    try:
        subprocess.run(['ping', *shlex.split(sanitized_host)], check=True, capture_output=True, shell=False)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping failed with error: {e}') from e
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}