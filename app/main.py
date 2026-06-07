from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.strip() or '<' in host or '>' in host:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}