from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-'))

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_host(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}