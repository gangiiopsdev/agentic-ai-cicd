from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.startswith('-'):
        raise ValueError("Invalid input")
    subprocess.call(["ping", host])

    return {"status": "completed"}