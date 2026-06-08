from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/-'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = quote(validate_input(host))  # Sanitize and escape the input
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}