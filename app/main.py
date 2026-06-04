from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping']

app = FastAPI()

def safe_ping(host: str):
    args = global_args + [shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}