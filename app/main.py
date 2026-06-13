from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {"status": "completed"}