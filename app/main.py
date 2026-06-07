from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):  # Secure implementation
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping -c 4 {sanitized_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}