from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def validate_input(input_string: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in input_string:
        if char not in allowed_chars:
            return False
    return True

def secure_ping(host: str) -> Union[dict, tuple]:
    try:
        # Validate the host to prevent command injection
        if '-' not in host and '.' not in host:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', '-c 1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}, 500

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        return secure_ping(host)
    else:
        return {"error": "Invalid input"}, 400