from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}

def is_valid_host(hostname: str) -> bool:
    # Simple validation logic (e.g., only allow alphanumeric and hyphens)
    return all(c.isalnum() or c == '-' for c in hostname)