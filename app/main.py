from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]
    with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}