from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {"status": "failed", "message": "Invalid input"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}