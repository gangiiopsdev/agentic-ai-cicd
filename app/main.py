from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if validate_host(host):
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host):
    # Add validation logic to ensure the host is safe
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True