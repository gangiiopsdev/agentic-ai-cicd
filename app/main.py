from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host input")
    # Using shell=False and passing args as a list to avoid shell injection risk
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}