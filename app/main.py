from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return False
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}