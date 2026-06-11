from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.split(host)
    subprocess.run(["ping", *safe_host], check=True, capture_output=True)
    return {"status": "completed"}