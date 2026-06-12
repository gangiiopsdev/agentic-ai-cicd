from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    safe_host = ''.join(c for c in host if c.isalnum() or c == '.').strip()
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}