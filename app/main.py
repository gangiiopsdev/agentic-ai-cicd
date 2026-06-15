from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host for allowed characters (e.g., alphanumeric and hyphen)
    if not all(c.isalnum() or c == '-' for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}