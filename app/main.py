from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return f'Host {host} is not allowed to be pinged.'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)