from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        return False
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": "Success"}
    else:
        return {"status": "failed", "error": "Invalid host"}