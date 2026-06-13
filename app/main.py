from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        command = ['ping', '-c', '4'] + shlex.split(sanitized_host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}