from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}