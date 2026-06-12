from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

# Additional preventive controls:
# 1. Validate and sanitize the input to ensure it does not contain malicious commands.
# 2. Use a whitelist of allowed hosts or use DNS resolution to validate the host's IP address.
# 3. Avoid using shell=True if possible, as it can lead to shell injection vulnerabilities.