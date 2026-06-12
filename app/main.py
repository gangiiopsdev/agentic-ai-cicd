from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def sanitize_input(input_str):
    # Enhanced sanitization
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', '!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '?', '/', ',', ';', ':'])

def sanitize_command(command):
    # Use subprocess.run with shell=False for better security
    return command.replace('{host}', shlex.quote(host))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}