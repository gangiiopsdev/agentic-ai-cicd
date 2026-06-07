from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use the ping utility with a hardcoded path to avoid command injection risks.
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_safe_host(host:
    # Implement logic to check if the host is safe
    # For example, allow only specific domains or IPs
    return True