from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.run(['ping', host], check=True)

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}