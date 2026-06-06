from fastapi import FastAPI
import subprocess

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', '-c', '1', sanitized_host]
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}