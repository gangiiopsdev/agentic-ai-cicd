from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}

# Function to validate the host input
def is_safe_host(host: str) -> bool:
    # Implement your validation logic here, e.g., regex or allowed list of hosts
    return True