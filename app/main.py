from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Unauthorized host"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}