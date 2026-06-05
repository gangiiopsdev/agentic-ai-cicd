from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError("Invalid host input")
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)