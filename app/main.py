from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if re.match(r'^[a-zA-Z0-9.-_]+$', sanitized_host):  # Add regex to validate host format
        args = ['ping', shlex.quote(sanitized_host)]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")