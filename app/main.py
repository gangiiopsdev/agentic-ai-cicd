from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() and e.isdigit())
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if validate_host(sanitized_host):
        cmd = ['ping', '-c', '1', sanitized_host]
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        return {'result': result.stdout}
    else:
        return {'error': 'Invalid host'}