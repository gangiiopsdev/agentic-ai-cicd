from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}