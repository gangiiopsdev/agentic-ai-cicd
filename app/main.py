from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(['ping', '-c', '1', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)