from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input before using it in the command
    if host.strip().isalnum():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)