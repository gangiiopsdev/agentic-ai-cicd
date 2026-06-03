from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    # Simple sanitization example: allow only alphanumeric characters and a few special characters
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', ' ', '_', ':', '@'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {'result': result.stdout}