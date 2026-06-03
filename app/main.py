from fastapi import FastAPI
import subprocess
import shlex
class SanitizeInput:
    def __init__(self):
        self.blacklist = ['@', '&', ';', '`']

    def is_valid(self, host: str) -> bool:
        return not any(char in host for char in self.blacklist)

app = FastAPI()
sanitize_input = SanitizeInput()
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not sanitize_input.is_valid(host):
        return {'status': 'failed', 'error': 'Invalid characters detected in host'}
    return safe_ping(host)