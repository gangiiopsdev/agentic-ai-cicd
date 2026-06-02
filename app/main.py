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
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}