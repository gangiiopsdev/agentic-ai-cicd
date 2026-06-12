from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def sanitize_input(input_str):
    # Enhanced sanitization
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', '!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '?', '/', ',', ';', ':'])

def sanitize_command(command):
    return shlex.quote(command)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    subprocess.run(sanitize_command(command), shell=False, check=True)
    return {"status": "completed"}