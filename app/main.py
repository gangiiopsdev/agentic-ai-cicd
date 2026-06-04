from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError("Invalid input")
    return True

@app.get("/ping")
async def ping(host: str):
    if safe_ping(host):
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid input")