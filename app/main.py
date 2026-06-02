from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid_host"}
    # Secure implementation using shlex.quote to escape special characters
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}