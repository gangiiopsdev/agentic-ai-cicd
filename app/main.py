from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run instead and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host):
    # Implement validation logic here to ensure the host is safe to ping
    return True