from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum():
        return {"error": "Invalid hostname"}
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)