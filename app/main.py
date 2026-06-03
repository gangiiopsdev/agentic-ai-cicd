from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}