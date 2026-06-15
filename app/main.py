from fastapi import FastAPI
import subprocess
from shlex import quote
import re

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, input_string))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host) is None:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}