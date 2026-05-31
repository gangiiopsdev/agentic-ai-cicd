from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')

@app.get="/ping")
def ping(host: str):
    # Secure implementation with input validation
    safe_ping(host)
    subprocess.call(['ping', host])
    return {'status': 'completed'}