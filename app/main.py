from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Add validation and sanitization for the host parameter
    if not validate_host(host):
        return 'Invalid host'
    return safe_ping(host)

# Function to validate and sanitize the host parameter
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., checking for allowed domains or IP addresses
    import re
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$|^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    return re.match(pattern, host) is not None