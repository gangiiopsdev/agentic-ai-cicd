from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def sanitize_host(host: str) -> str:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(c for c in host if c in allowed_chars)
        return sanitized_host

def is_valid_ip(ip: str) -> bool:
    try:
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Validate input to prevent command injection
    if is_valid_ip(host) or '.' in host:
        args = ['ping', SafePing.sanitize_host(host)]
        subprocess.run(args, check=True, shell=False)
    else:
        raise ValueError('Invalid host format')

    return {'status': 'completed'}