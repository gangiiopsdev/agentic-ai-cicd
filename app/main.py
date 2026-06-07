from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex.quote to sanitize the input
    safe_host = shlex.quote(host)
    subprocess.run(["ping", safe_host], check=True, shell=False)
    return {"status": "completed"}