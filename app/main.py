from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using shlex to safely construct the command
    import shlex
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}