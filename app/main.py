from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}

    args = ['ping', host]
    subprocess.call(args)

    return {'status': 'completed'}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed domains or IP addresses
    return True