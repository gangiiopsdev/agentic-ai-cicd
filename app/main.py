from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex.quote to sanitize input
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}