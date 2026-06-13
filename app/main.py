from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen to prevent shell injection
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}