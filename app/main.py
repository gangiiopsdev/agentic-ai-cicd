from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host or not isinstance(host, str):
        return {"status": "invalid_input"}
    # Fixed implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}