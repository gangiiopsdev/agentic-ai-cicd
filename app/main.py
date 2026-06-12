from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {"error": "Invalid host"}
    subprocess.run(['ping', '-c 1', host], check=True)
    return {"status": "completed"}