from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    cmd = ['ping', sanitized_host]
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}