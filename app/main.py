from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError("Invalid host format")

    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}