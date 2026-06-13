from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.isalnum():
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}