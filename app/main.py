from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

cimport = subprocess.CalledProcessError

def safe_ping(host: str):
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except cimport as e:
        return {"status": "failed", "error": e.stderr}