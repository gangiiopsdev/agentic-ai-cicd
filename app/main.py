from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Splitting host into separate arguments to prevent shell injection
    args = shlex.split(host)
    subprocess.call(["ping"] + args, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}