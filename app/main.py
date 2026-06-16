from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if '.' in host:
        return False
    subprocess.call(['ping', host])
    return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "message": "Invalid input"}
    return {"status": "completed"}