from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def sanitize_host(host: str) -> str:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(c for c in host if c in allowed_chars)
        return sanitized_host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Sanitize input to prevent command injection
    args = ['ping', SafePing.sanitize_host(host)]
    subprocess.run(args, check=True, shell=False)

    return {'status': 'completed'}