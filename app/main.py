from fastapi import FastAPI
import subprocess
import shlex
import re

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', '!', '?', ','])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9-.!? ,]*$', sanitized_host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}