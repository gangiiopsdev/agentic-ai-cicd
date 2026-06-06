from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a whitelist of allowed hosts or implement proper validation and sanitization
    allowed_hosts = {'allowed_host1', 'allowed_host2'}
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', str(4), host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)