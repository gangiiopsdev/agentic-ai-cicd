from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "message": "Invalid host"}
    return {"status": "completed"}