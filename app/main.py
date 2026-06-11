from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input')
    # Use a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])

    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'