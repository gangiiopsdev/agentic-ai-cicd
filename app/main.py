from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}