from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}