from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to safely handle the host string
    safe_host = shlex.quote(host)
    if safe_host.isalnum() and '-' in safe_host:
        subprocess.run(['ping', safe_host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host name"}