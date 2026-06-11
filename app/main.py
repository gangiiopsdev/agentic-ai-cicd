from fastapi import FastAPI
import subprocess
git add
app = FastAPI()

def safe_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use a whitelist of allowed hosts or validate the input more strictly
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return safe_ping(host)