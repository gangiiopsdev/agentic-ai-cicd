from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead of shell=True for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "output": status}