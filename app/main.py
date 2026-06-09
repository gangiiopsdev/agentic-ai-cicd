from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use absolute path for 'ping' to mitigate risks
        output = subprocess.run(['/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'''

def validate_host(host: str):
    # Simple validation to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}