from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=True
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}