from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ["ping", *shlex.split(host)]
    subprocess.call(command, shell=False)
    
    return {"status": "completed"}