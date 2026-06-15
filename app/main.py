from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def sanitize_input(value):
    return ''.join(e if e.isalnum() or e in ('.', '-', '_') else '_' for e in value)

def run_command(command, *args):
    full_command = [command] + list(map(quote, args))
    try:
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.stderr)}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return run_command('ping', sanitized_host)