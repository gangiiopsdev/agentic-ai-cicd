from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True, timeout=5)
    return {'status': 'completed'}