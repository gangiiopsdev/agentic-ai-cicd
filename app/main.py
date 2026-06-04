from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid or unauthorized host name")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}