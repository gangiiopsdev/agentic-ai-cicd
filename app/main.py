from fastapi import FastAPI
import subprocess
import shlex
import re

class SafeInput:
    def __init__(self, allowed_chars: str):
        self.allowed_chars = allowed_chars

    def sanitize(self, input_str: str) -> str:
        return ''.join(char for char in input_str if char in self.allowed_chars)

app = FastAPI()

@app.get('/ping/')
def ping(host: str):
    safe_input = SafeInput(allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    sanitized_host = safe_input.sanitize(host)
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}