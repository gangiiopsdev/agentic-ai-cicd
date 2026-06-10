from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr.decode()}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if is_valid_host(host):
        return safe_ping(host)
    else:
        return {"status": "failed", "error": "Invalid host format"}

# Function to validate and sanitize host input
def is_valid_host(host: str) -> bool:
    import re
    # Regular expression to match valid IP addresses and domain names
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}|localhost|::1)$
    return re.match(pattern, host) is not None