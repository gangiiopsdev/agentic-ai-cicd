from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": result.stderr}
    except subprocess.TimeoutExpired:
        return {"status": "failed", "error": "Timeout occurred"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)