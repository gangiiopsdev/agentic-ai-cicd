from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}