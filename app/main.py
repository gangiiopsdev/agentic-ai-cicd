from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    # Sanitize the host input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host input"}

    call = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": call.stdout}