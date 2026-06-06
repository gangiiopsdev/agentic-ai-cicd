from fastapi import FastAPI
import shlex
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')
    return shlex.split(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')

    sanitized_host = safe_ping(host)
    command = ['ping', *sanitized_host]
    subprocess.run(command, check=True, shell=False)  # Ensure shell=False is explicitly set

    return {'status': 'completed'}