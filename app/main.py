from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        return False
    sanitized_host = subprocess.quote(host)
    return subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is False:
        return {"status": "failed", "message": "Invalid input"}
    return {"status": "completed", "output": result.stdout}