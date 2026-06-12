from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    sanitized_host = host.strip()
    if not sanitized_host:
        return {"status": "invalid host"}
    try:
        subprocess.run(["ping", sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}