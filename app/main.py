from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_')
    return ''.join(c for c in input_str if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(['ping', quote(sanitized_host)], shell=False, check=True)
    return {"status": "completed"}