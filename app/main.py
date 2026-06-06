from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here (e.g., allowed IP ranges, domain names)
    if not host.isalnum():
        return False
    return True

@app.get="/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}