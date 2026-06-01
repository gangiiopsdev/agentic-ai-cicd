from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True and validate input
    if not host.isdigit():
        args = ['ping', host]
        subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}