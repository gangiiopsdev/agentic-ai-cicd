from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Validate host to ensure it only contains valid characters and is not a potential command
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError("Invalid input for host")
    subprocess.run(['ping', sanitized_input(host)], check=True, shell=False)
    return {"status": "completed"}