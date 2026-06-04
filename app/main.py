from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host parameter
    if not host.isalnum():
        raise ValueError('Invalid hostname')

    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)