from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', safe_ping(host)]
    subprocess.call(args)
    return {"status": "completed"}