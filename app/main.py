from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):  # Fixed implementation
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ["ping", *shlex.split(host)]
    try:
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}