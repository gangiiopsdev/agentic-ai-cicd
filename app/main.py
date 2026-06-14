from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}