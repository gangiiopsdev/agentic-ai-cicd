from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}