from fastapi import FastAPI
import subprocess
globally_allowed_ips = {"127.0.0.1", "8.8.8.8"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_ips:
        subprocess.run(["ping", host], check=True)
    else:
        raise ValueError("IP not allowed")
    return {"status": "completed"}