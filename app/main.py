from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' 
    if all(char in allowed_chars for char in host) and len(host) <= 255:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Secure implementation
        subprocess.run(['ping', cmd_quote(host)], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400