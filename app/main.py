from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return "Invalid host"
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'test.example.com']  # Example list of allowed hosts
    return host in allowed_hosts