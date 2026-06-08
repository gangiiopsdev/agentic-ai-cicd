from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the input
    if not host.isalnum():
        return {"status": "invalid host"}
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}