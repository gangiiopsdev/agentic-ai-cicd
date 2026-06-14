from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return 'Invalid host'
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Basic validation, replace with a more robust solution as needed
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts