from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Use safe subprocess call without shell=True
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}