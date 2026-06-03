from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it is safe
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)