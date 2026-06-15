from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.run for better control and safety
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'error', 'output': 'Host parameter is required'}
    # Validate the host input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid host'}
    # Use a whitelist of safe hosts and sanitize input
    if host not in ['example.com', 'localhost']:
        return {'status': 'error', 'output': 'Invalid host'}
    return safe_ping(host)