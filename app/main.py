from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = shlex.split(f'ping {sanitized_host}')
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}