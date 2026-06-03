from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}