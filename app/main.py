from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    return subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}