from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    command = ['ping', host]
    subprocess.call(command)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}