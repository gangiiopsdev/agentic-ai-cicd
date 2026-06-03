from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    cmd = ['ping'] + shlex.split(host)
    subprocess.run(cmd, check=True)
    return {"status": "completed"}