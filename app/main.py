from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    if not host.strip() or any(char in host for char in [';', '&', '|', '`']):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {"status": "completed"}