from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        return subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "output": result.stderr}