from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = 'ping {}
    subprocess.call(shlex.split(command))
    return {'status': 'completed'}