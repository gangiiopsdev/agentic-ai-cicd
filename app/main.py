from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}