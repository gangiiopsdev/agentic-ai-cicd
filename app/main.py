from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Ensure host input is a valid IP address
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"status": "failed", "error": "Invalid host format"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "result": result.stdout}