from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.strip():
        return False
    sanitized_host = shlex.quote(host)
    ping_command = ['ping', sanitized_host]
    result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        if not status:
            return {"status": "failed"}
        return {"status": "completed", "output": status}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}