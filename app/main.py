from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if validate_host(host):
        subprocess.call(args, shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts