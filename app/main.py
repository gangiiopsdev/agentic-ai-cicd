from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safely construct the ping command using shlex.quote
    cmd = ['ping', shlex.quote(host)]
    subprocess.call(cmd)

@app.get("/ping")
def ping(host: str):

    safe_ping(host)

    return {"status": "completed"}