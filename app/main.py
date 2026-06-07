from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}