from fastapi import FastAPI
import subprocess32 as subprocess
cimport subprocess32 as subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError("Invalid host input")

    sanitized_host = subprocess32.list2cmdline([host])
    result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}