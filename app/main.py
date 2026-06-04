from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    safe_host = host.strip()
    if safe_host and "" not in safe_host:
        subprocess.call(['ping', safe_host])
    return {"status": "completed"}