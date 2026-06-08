from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        return False
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host"}