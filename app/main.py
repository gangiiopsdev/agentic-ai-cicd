from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host and all(c.isalnum() or c in "-_" for c in host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}