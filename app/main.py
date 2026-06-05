from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() and '0' <= c <= '9')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation with input validation and escaping
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, capture_output=True)
    return {'status': 'completed'}