from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious content
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host input"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}