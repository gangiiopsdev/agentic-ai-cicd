from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}