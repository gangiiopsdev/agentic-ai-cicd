from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['192.168.0.1', '10.0.0.1']  # Add more hosts as needed
    return host in allowed_hosts