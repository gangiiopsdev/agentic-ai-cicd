from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host input is safe by validating and sanitizing it
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    sanitized_host = subprocess.quote(host)
    return subprocess.call(['ping', sanitized_host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}