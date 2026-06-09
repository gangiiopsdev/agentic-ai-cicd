from fastapi import FastAPI
import subprocess
global host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.isalnum() or len(host) > 20:
        return {"error": "Invalid host"}

    # Secure implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}