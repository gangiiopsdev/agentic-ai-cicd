from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shlex for safely handling arguments
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}