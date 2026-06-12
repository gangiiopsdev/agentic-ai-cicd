from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if host.startswith('192.168.'):)
        safe_host = ''.join(c for c in host if c.isdigit() or c == '.').strip()
        subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}