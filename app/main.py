from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isalnum():
        raise ValueError('Invalid host name')

    subprocess.call(['ping', '--'], [host])

    return {"status": "completed"}