from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a whitelist of allowed hosts or implement proper validation and sanitization
    if host not in ['allowed_host1', 'allowed_host2']:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)