from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.strip():
        subprocess.call(["ping", host])
    else:
        return {"status": "invalid input"}
    
    return {"status": "completed"}