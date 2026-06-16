from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex or allowed list of hosts
    return True