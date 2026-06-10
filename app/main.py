from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using a list for args instead of shell=True and validating the host parameter
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

def is_valid_host(host):
    # Simple validation, replace with more robust checks as needed
    return all(c.isalnum() or c in '-.' for c in host)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}