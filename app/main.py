from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and len(host) <= 3:
        return subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)