from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.strip():
        return False
    ping_command = ['ping', *shlex.split(host)]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    if not status:
        return {"status": "failed"}
    return {"status": "completed", "output": status}