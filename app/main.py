from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation with input validation
    if not host.isalnum() or len(host) > 64:
        return {"error": "Invalid host name"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}