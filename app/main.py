from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping(host: str):
    subprocess.run(['ping', host], check=True, text=True)  # Ensure input is sanitized
    return {"status": "completed"}