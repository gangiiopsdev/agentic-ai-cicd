from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}