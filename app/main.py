from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum() or len(host) > 100:
        return 'Invalid host'
    # Use a whitelist of allowed hosts or implement more robust validation
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return 'Host not allowed'
    return execute_ping(host)