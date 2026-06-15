from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Safer implementation with input validation
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {"status": "completed"}