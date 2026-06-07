from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-]{1,}$'
    return re.match(pattern, host) is not None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        try:
            args = shlex.split(f'ping -c 4 {sanitized_host}')
            output = subprocess.check_output(args, timeout=5, stderr=subprocess.STDOUT, shell=False)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": e.output.decode()}
    else:
        return {"status": "error", "error": "Invalid host input"}