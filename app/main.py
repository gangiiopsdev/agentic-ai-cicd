from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if host.strip().endswith('.localdomain'):
        safe_host = ''.join(e for e in host if e.isalnum() or e in '.-')
        subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed'}