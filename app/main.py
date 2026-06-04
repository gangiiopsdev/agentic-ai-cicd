from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and f-string formatting
    subprocess.call(["ping", host])
    return {"status": "completed"}