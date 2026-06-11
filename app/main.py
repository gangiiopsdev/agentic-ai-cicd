from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid hostname')
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], check=True, text=True)
    return {'status': 'completed'}