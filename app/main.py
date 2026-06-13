from fastapi import FastAPI
import subprocess
import re

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    regex = r'^[a-zA-Z0-9.-_]+$'
    if re.match(regex, host):
        return True
    return False