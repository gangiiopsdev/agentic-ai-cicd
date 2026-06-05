from fastapi import FastAPI
import subprocess
from typing import List
import shlex

class CommandSanitizer:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'

    def sanitize_command(self, command: str) -> str:
        return ''.join(char for char in command if char in self.allowed_chars)

app = FastAPI()

command_sanitizer = CommandSanitizer()

@app.get('/ping')
def ping(host: str):
    sanitized_host = command_sanitizer.sanitize_command(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', '-c 1'] + shlex.split(sanitized_host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}