from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and args instead of shell=True
    if 'localhost' in host or '127.0.0.1' in host:
        subprocess.run(['ping', host], check=True)
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}