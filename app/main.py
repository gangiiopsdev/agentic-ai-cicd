from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or ' ' in host:
        return {"status": "invalid_input", "message": "Invalid host name"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}