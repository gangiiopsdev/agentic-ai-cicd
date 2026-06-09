from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Add a whitelist of allowed hosts
        return safe_ping(host)
    else:
        return {"status": "failed", "error": "Invalid host"}