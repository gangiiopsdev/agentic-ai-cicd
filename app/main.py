from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in user_input if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}