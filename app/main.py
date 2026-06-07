from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}