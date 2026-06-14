from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host name")

    # Secure implementation with shell=False
    subprocess.call(["ping", host], shell=False)

    return {"status": "completed"}