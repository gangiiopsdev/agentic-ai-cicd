from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_fixed(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')
    # Use a safe method for pinging
    subprocess.run(['ping', '-c', '1', host], check=True)