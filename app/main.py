from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

# Define a function to validate the host input
def validate_host(host):
    # Add validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts