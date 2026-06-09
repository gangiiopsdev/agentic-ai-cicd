from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and shlex.quote for safe string handling
    subprocess.run(["ping", shlex.quote(host)], check=True)
    return {"status": "completed"}