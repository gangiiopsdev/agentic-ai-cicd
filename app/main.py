from fastapi import FastAPI
import subprocess
import ipaddress
def is_safe_host(host):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}