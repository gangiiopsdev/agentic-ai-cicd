from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call([cimport('ping'), host])
    return {"status": "completed"}