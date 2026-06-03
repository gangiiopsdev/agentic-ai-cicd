from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Add validation logic for the host parameter
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not is_valid_host(host):\n        return {"error": "Invalid host"}\n    subprocess.call(['ping', "/sbin/ping", host])\n    return {"status": "completed"}