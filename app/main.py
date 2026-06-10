from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' not in host or '.' not in host:
        return False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.returncode == 0

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid input for ping"}