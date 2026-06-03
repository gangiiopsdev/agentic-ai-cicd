from fastapi import FastAPI
import subprocess
import shlex
class PingHostValidator:
    @staticmethod
def validate_host(host: str):
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
        if not all(char in allowed_chars for char in host) or '.' not in host:
            raise ValueError('Invalid host input')

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    PingHostValidator.validate_host(host)
    # Use a safe method to validate and format the host before passing it to subprocess
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}