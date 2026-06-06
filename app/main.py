from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}