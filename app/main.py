from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {"status": "failed", "message": "Invalid host name"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}