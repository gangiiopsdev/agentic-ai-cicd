from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host input")
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}