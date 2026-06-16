from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def sanitize_host(host: str) -> str:
        return ''.join(c for c in host if c.isalnum())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = SafeSubprocess.sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {'status': 'completed'}