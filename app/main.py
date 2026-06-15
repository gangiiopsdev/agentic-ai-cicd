from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return "Invalid host"
    return _ping(host)

def is_valid_host(host):
    allowed_hosts = ["google.com", "example.com"]  # Example of allowed hosts
    return host in allowed_hosts