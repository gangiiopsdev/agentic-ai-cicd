from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely escape command arguments
    safe_host = shlex.quote(host)
    subprocess.call(f"ping {safe_host}", shell=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}