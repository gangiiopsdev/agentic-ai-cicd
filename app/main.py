from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list of arguments
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"error": "Invalid characters in hostname"}
    safe_ping(host)
    return {"status": "completed"}