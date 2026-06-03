from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    # Improved sanitization example: allow only alphanumeric characters, hyphens, and periods
    return ''.join(c for c in input_string if c.isalnum() or c == '-' or c == '.').strip()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}