from fastapi import FastAPI
import subprocess
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        return {"status": "invalid_host"}
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}