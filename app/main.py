from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()
    if not all(c.isalnum() or c in ['-', '.', '_', '@'] for c in safe_host):  # Basic validation
        raise ValueError('Invalid host name')
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}