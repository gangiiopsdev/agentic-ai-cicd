from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run with explicit arguments for security
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Call the safe function instead of using shell=True
    safe_ping(host)
    return {"status": "completed"}