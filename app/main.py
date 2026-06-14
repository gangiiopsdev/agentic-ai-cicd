from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and escaping
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}