from fastapi import FastAPI
import subprocess
def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.run(['ping', '--', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}