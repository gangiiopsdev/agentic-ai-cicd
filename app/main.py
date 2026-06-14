from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization, should be more robust for production use
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use subprocess.run instead of subprocess.call and validate the command
    cmd = shlex.split(f'ping -c 1 {sanitized_host}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}