from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.Popen with a tuple of arguments
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host"}, 400

    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}