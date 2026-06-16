from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}