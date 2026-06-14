from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255 or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex.quote to safely quote the input
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {'message': 'Pong'}
    except Exception as e:
        return {'error': str(e)}