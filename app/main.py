from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping', '{}']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = global_args.copy()
    args[1] = host
    subprocess.call(args)
    return {"status": "completed"}