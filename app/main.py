from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' not in host:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}