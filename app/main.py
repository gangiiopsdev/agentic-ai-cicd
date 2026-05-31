from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or host.isnumeric() or '.' in host:
        return None
    return host

@app.get("/ping")
def ping(host: str):
    safe_host = safe_ping(host)
    if safe_host is None:
        return {"status": "failed", "error": "Invalid input for ping"}
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}