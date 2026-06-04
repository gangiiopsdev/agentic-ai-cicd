from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in input_string if char in allowed_characters)
    return sanitized[:255]

def validate_host(host):
    # Validate the host format to prevent command injection
    import re
    pattern = r'^[a-zA-Z0-9-.]+$'
    return re.match(pattern, host) is not None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Sanitize user input to prevent command injection
        host = sanitize_input(host)
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host format"}