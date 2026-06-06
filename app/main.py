from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Ensure host is validated or sanitized before use
    if not host.isdigit():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)