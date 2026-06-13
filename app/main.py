from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using a safe command
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}