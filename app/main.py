from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return 'Host not allowed'
    return safe_ping(host)