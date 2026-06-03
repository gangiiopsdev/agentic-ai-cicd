from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it's a valid IP address or hostname
    if not is_valid_host(host):
        return {"status": "error", "result": "Invalid host"}
    result = run_ping(host)
    return {"status": "completed", "result": result}
def is_valid_host(host):
    # Simple regex to validate IP address and hostname
    import re
    ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    hostname_pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return ip_pattern.match(host) or hostname_pattern.match(host)