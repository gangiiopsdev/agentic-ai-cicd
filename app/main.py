from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def validate_host(host: str):
    # Implement a simple validation function to ensure the input is safe
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts