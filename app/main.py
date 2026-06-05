from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    if not input_str:
        return None
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_str if char in safe_chars)

def is_valid_host(host):
    pattern = re.compile(r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or not is_valid_host(sanitized_host):
        return {"status": "error", "message": "Invalid host parameter"}
    result = subprocess.run(['ping', '-c 1', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}