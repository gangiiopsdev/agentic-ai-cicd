from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    command_parts = ['ping', *shlex.split(host)]
    subprocess.call(command_parts)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}