from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        ipaddress.ip_address(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ipaddress.AddressValueError) as e:
        return {"status": "error", "output": str(e)}