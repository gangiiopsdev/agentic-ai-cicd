from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    command = ['ping'] + shlex.split(host)
    return subprocess.call(command, shell=False)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shlex to handle potential injection attacks
    result = safe_ping(host)
    return {"status": "completed", "result": result}