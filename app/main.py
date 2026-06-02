from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    safe_args = ' '.join(shlex.quote(arg) for arg in args)
    subprocess.run(safe_args, check=True, shell=True)
    return {"status": "completed"}