from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError("Invalid host name")
    subprocess.call(['ping', host])

    return {"status": "completed"}