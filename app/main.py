from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host):
        raise ValueError('Invalid hostname')

    # Use subprocess with shell=False and avoid shlex.split
    command = ['ping', host]
    result = subprocess.run(command, check=True, text=True, capture_output=True)

    return {'status': 'completed', 'output': result.stdout}