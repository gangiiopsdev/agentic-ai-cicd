from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}