from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    sanitized_host = host.strip().replace(' ', '_')
    subprocess.call(["ping", sanitized_host])

    return {"status": "completed"}