from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)