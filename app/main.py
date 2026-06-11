from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and '.' in host:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {"status": "completed"}