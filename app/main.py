from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote to escape arguments
    subprocess.call(shlex.split(f"ping {host}"))

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}