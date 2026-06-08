from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid IP address or hostname
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return "Invalid host"
    return safe_ping(host)