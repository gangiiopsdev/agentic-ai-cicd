from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(f'ping {host}', shell=False)
    return {'status': 'completed'}