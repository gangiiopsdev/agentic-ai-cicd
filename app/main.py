from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with sanitized input
    safe_host = shlex.quote(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}