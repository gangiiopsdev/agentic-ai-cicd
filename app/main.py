from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}