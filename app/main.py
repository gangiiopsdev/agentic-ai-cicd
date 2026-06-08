from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join([char for char in input_string if char in allowed_chars])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum():  # Basic validation to prevent injection
        raise ValueError('Invalid input for host')
    subprocess.run(['ping', quote(sanitized_host)], check=True, capture_output=True)
    return {'status': 'completed'}