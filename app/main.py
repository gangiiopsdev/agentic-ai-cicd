from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use a safe command
    safe_host = host.strip()[:100]  # Limit length to prevent excessive input
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}