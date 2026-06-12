from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    subprocess.call(["ping", host])

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}

    return {"status": "completed"}