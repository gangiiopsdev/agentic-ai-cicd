from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the input to avoid command injection
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)