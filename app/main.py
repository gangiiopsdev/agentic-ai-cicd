from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with list of args
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}