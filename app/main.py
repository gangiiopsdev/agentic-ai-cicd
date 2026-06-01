from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/ping")
def ping_fixed(host: str):
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}