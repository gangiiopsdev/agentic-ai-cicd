from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char if char in allowed_chars else '_' for char in user_input)
    return sanitized
def safe_ping(host: str):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return safe_ping(sanitized_host)