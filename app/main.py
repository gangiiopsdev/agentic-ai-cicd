from fastapi import FastAPI
import subprocess
from shlex import quote
import os

current_user = os.getenv('USER') or 'nobody'

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    result = subprocess.run(['ping', '-c 1', f'@{current_user}@{sanitized_host}'], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}