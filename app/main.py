from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}