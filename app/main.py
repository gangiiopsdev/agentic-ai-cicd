from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host parameter
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic
    if host not in allowed_hosts:
        return "Invalid input"
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts or validate against known good patterns
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic
    if host not in allowed_hosts:
        return "Invalid input"
    return safe_ping(host)