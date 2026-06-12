from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return "Invalid input"
    # Use a whitelist of allowed hosts instead of sanitizing the input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return "Invalid host"
    return run_ping(host)