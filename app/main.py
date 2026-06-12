from fastapi import FastAPI
import shlex
import os
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

def validate_executable_path(path):
    return path.startswith('/bin/') or path.startswith('/usr/bin/')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(sanitize_input(host))
    if not validate_executable_path('ping'):
        raise ValueError('Unsafe executable path used')
    try:
        subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}