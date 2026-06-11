from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:-')
    return ''.join(c for c in input_str if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or '.' not in sanitized_host:
        raise ValueError('Invalid host name')
    command = ['ping', shlex.quote(sanitized_host)]
    with subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}