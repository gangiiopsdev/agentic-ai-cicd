from fastapi import FastAPI
import subprocess
import shlex
import re

global ALLOWED_CHARS
ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.fullmatch(ALLOWED_CHARS, host):  # Use regex to ensure input is allowed
        return {"status": "error", "message": "Invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}