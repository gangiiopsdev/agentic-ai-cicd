from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' 
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {'status': 'completed'}