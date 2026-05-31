from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}