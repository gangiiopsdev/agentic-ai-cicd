from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is a valid IP address or domain name
    return True