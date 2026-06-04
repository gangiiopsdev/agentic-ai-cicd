from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def valid_host(host):
    # Implement validation logic here, e.g., regex check for allowed hostnames/IPs
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None