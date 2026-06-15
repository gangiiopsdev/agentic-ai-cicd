from fastapi import FastAPI
import subprocess
import shlex

glitchy_api = FastAPI()

@glitchy_api.get("/ping")
def ping(host: str):
    args = ['ping', host]
    subprocess.run(shlex.split(' '.join(args)), check=True)
    return {"status": "completed"}