from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400