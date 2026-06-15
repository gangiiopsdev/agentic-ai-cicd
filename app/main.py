from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return run_ping(host)
    else:
        return {'error': 'Host not allowed'}