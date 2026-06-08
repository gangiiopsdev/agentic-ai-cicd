from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run for argument escaping
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}