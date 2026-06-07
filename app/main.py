from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}

    try:
        subprocess.call(["ping", host])
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}