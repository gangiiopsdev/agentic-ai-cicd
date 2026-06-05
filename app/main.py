from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get("/ping")
def ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'error', 'message': 'Invalid input'}
    sanitized_host = sanitize_input(host)
    result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}