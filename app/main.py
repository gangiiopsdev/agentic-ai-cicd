from fastapi import FastAPI
import subprocess
import re
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda char: char in allowed_chars, input_string))

def validate_host(host: str):
    # Validate the host format to ensure it does not contain dangerous characters
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    if not pattern.match(host):
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_input(host)
    validate_host(sanitized_host)
    # Safe to use the sanitized and validated host
    subprocess.run(['ping', sanitized_host], check=True)