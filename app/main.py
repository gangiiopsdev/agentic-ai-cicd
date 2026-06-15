from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid host input"}
    # Secure implementation using subprocess.run with shell=False and args parameter
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}