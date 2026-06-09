from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode != 0:
        raise Exception('Ping failed')
    return {"status": "completed", "output": result.stdout}