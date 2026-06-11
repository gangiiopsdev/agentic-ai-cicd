from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    # Secure implementation using subprocess.run with shell=False and verify input
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}