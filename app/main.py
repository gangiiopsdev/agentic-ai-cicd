from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it's a valid IP address or hostname
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"status": "failed", "error": "Invalid host"}

    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}