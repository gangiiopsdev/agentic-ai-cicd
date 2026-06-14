from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    ping_safe(host)
    return {"status": "completed"}