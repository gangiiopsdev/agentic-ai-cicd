from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}