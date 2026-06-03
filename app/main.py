from fastapi import FastAPI
import subprocess
import shlex
cimport re

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_input = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized_input

def validate_host(host):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        validate_host(host)
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}