from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "invalid_host"}
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)
    return {"status": "completed"}