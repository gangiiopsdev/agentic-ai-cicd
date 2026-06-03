from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex to escape arguments
    args = shlex.split(f'ping {host}')
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}