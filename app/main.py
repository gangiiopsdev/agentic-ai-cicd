from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use ping -c 1 to limit the number of pings and avoid potential DoS attacks
    command = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_safe_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domain names or IP addresses
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts