from fastapi import FastAPI
import subprocess
import ipaddress
global host_whitelist = {"192.168.1.1", "10.0.0.1"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Ensure host input is a valid IP address and in the whitelist
    try:
        ip_address = ipaddress.ip_address(host)
    except ValueError:
        return {"status": "failed", "error": "Invalid host format"}
    if ip_address not in host_whitelist:
        return {"status": "failed", "error": "Host not allowed"}
    result = subprocess.run(['ping', '-c', '1', str(ip_address)], capture_output=True, text=True, check=True)
    return {"status": "completed", "result": result.stdout}