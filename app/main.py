from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    safe_ping(host)

    return {"status": "completed"}