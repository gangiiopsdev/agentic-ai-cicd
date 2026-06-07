from fastapi import FastAPI
import subprocess
from shlex import quote
from os.path import basename

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char if char in allowed_chars else '' for char in input_string)

def validate_host(host):
    return basename(host) == host and len(host) <= 30

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}