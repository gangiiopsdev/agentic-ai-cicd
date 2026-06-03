from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def sanitize_input(host: str) -> str:
    return ''.join(char for char in host if char.isalnum() and ord(char) <= 127)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {'status': 'error', 'error': 'Invalid input'}
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}