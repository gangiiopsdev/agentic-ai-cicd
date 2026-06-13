from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with full path and input validation to prevent shell injection
    if not host or not host.isalnum():
        return {"status": "invalid host"}, 400
    subprocess.run(['/bin/ping', host], check=True)
    return {"status": "completed"}