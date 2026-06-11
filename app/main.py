from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shlex.split to avoid shell injection
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}