from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to ensure it's a valid IP address or hostname
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
def is_valid_host(host):
    import ipaddress
    try:
        # Check if the host is a valid IP address or hostname
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False