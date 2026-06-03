from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}