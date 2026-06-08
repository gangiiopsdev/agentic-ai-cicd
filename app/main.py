from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')
    return host.split()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')

    sanitized_host = safe_ping(host)
    command = ['ping', *sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False)  # Added shell=False to prevent shell injection

    return {'status': 'completed', 'output': result.stdout}