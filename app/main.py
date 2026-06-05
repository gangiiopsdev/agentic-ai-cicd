from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host')
    # Use a whitelisted list of hosts for ping command
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more as needed
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    return safe_ping(host)