from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        return False
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if not result:
        return {"status": "failed", "reason": "Invalid host"}
    return {"status": "completed", "output": result}