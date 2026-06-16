from fastapi import FastAPI
import subprocess
cimport ipaddress

app = FastAPI()

def execute_ping(host: str):
    try:
        # Validate the host to ensure it is a valid IP address or hostname
        if not ipaddress.ip_address(host) and not ipaddress.ip_network(host):
            return {'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return f'Error: {e.stderr}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 100:
        return {"error": "Invalid host"}
    return execute_ping(host)