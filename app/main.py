from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {"error": "Invalid host"}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hosts or IP ranges
    allowed_hosts = ["example.com", "127.0.0.1"]
    import ipaddress
    try:
        if ipaddress.ip_address(host).is_private:
            return False
        return host in allowed_hosts
    except ValueError:
        return False