from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    output = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": output.stdout}