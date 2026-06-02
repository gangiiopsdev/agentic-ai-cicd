from fastapi import FastAPI
import subprocess
from shlex import quote

global app
app = FastAPI()


def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ('-', '.', '_', ':', '/', '@'))

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host:
        subprocess.call(["ping", quote(sanitized_host)])
    else:
        return {"status": "invalid input"}
    return {"status": "completed"}