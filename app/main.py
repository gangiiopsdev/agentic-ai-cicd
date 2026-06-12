from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c 1'] + [sanitized_host]  # Limit the number of pings to avoid abuse
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed'}