from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    try:
        subprocess.call(["ping", host], shell=False)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}