from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.call(f"ping {host}", shell=False)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}
    return {"status": "completed"}