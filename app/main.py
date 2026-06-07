from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}