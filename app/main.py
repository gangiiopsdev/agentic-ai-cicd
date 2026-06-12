from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe to use with ping
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', '192.168.1.1']  # Example list of allowed hosts
    return host in allowed_hosts