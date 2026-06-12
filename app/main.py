from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using a list to avoid shell=True, which prevents command injection
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}