from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe for the ping command
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

# Function to validate the host input
def is_safe_host(host: str) -> bool:
    # Simple validation, replace with more robust checks as needed
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts