from fastapi import FastAPI
import subprocess
import shlex

class Sanitizer:
    def __init__(self, allowed_chars):
        self.allowed_chars = allowed_chars

    def sanitize(self, user_input):
        return ''.join(c for c in user_input if c in self.allowed_chars)

app = FastAPI()
sanitizer = Sanitizer('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitizer.sanitize(shlex.split(host)[0])  # Use shlex to split and sanitize the host input
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': e.stderr}