from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').isdigit() and len(host) > 1

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    # Fixed implementation using subprocess.run with shell=False and proper argument passing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}