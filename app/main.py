from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and escape input to prevent shell injection
    host = shlex.quote(host)
    subprocess.call(["ping", host])
    return {"status": "completed"}