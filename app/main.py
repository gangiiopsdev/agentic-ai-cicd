from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Sanitize host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization of the output before using it in subprocess call
    safe_ping(host)
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in '.-')
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}