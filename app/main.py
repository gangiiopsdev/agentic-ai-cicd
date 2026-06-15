from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)

def safe_ping(host: str):
    if validate_host(host):
        command = ['ping', '-c', '1', shlex.quote(host)]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)