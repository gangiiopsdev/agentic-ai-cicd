from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Sanitize input and use full executable path
    if 'ping' in host or any(char in host for char in [';', '&', '|', '<', '>']):
        raise ValueError('Invalid input')
    subprocess.run(['/sbin/ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}