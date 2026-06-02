from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        subprocess.run(["ping", host], check=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic
    allowed_hosts = ["example.com", "another.example.com"]
    return host in allowed_hosts