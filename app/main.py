from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if len(sanitized_host) > 20:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', '-c', '1'] + shlex.split(sanitized_host), check=True, capture_output=True, text=True)
    return {'status': 'completed'}