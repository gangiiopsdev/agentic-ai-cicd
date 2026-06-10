from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization: only allow alphanumeric characters and a limited set of allowed characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Secure implementation using subprocess.run with shell=False and safe arguments
    result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}