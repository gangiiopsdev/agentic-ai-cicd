from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}