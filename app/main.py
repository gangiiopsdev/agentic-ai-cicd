from fastapi import FastAPI
import subprocess

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}