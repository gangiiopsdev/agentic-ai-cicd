from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(args, shell=False)
    return {"status": "completed"}