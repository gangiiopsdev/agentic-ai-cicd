from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid input for host")
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    try:
        subprocess.call(shlex.split(f'ping {host}'), shell=False)
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}