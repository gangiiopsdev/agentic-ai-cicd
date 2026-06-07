from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import os

class SanitizedHost(subprocess.SubprocessError):
    pass

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):,
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run([os.path.join(os.getcwd(), 'ping'), cmd_quote(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}