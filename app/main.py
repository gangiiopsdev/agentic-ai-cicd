from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}

def validate_host(host: str):
    # Add validation logic here, e.g., checking for allowed IP ranges or domain formats.
    allowed_hosts = ['192.168.1.0/24', 'example.com']
    return any(host in network for network in allowed_hosts)