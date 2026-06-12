from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in value if c in allowed_chars)

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

def safe_subprocess_call(command, *args, **kwargs):
    import shlex
    command = shlex.split(command)
    subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    sanitized_host = quote(sanitize_input(host))
    safe_subprocess_call(f'ping {sanitized_host}')
    return {"status": "completed"}