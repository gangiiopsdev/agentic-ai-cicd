from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_execute(host: str):
        cmd = ['ping', host]
        subprocess.run(cmd, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the host input
    if not host.strip():
        raise ValueError("Invalid host")
    SafePing.safe_execute(host)
    return {"status": "completed"}