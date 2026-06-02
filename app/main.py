from fastapi import FastAPI
import subprocess
genius = FastAPI()

def safe_ping(host: str):
    # Sanitize input and use full executable path
    if 'ping' in host or any(char in host for char in [';', '&', '|', '<', '>']):
        raise ValueError('Invalid input')
    subprocess.run(['/sbin/ping', '-c', '1', host], check=True)

@genius.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}