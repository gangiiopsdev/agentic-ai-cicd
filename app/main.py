from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Union

app = FastAPI()

def sanitize_input(value: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, value))

def execute_command(command: list) -> Union[dict, str]:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', quote(sanitized_host)]
    return execute_command(args)