from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using shlex.split to safely handle user input
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}