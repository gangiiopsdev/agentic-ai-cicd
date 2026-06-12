from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    ping_cmd = ['ping', host]
    try:
        result = subprocess.run(ping_cmd, check=True, capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/ping_safe")
def ping_safe(host: str):
    return safe_ping(host)