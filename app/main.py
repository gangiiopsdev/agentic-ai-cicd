from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(["ping", host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {"status": "completed"}
def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe
    return True