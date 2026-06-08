from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using list for arguments to prevent shell injection
    args = ['ping', host]
    subprocess.run(shlex.split(' '.join(args)), check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}