from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return False
    args = ['ping', host]
    # Use shell=False and pass args as a list to avoid shell injection
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}