from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate 'host' to prevent command injection
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host):
    # Add your validation logic here, e.g., regex check for IP or domain name
    import re
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    domain_pattern = r'^[a-zA-Z0-9-]+([.][a-zA-Z0-9-]+)*$'
    return re.match(ip_pattern, host) or re.match(domain_pattern, host)