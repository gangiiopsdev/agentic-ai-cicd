from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    # Sanitize input to prevent command injection
    allowed_hosts = {"example.com", "another-example.com"}
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(["ping", host], check=True)
    return {"status": "completed"}