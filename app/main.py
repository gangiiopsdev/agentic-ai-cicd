from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
    return {
        "status": "completed"
    }