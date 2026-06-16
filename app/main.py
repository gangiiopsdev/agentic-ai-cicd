from fastapi import FastAPI
import subprocess
import re

app = FastAPI()
allowed_hosts = ['example.com', '192.168.1.1']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}