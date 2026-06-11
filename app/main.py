from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', shlex.quote(host)]  # Use '-c' for specifying the count of pings
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping failed with error: {e}') from e

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "message": str(e)}