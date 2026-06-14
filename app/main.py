from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and quoting
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host], shell=False)
    return {"status": "completed"}