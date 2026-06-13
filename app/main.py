from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if host.startswith('127.0.0.1') or host.startswith('localhost'):
            return {'status': 'completed', 'output': ''}
        else:
            try:
                output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
                return {'status': 'completed', 'output': output.stdout}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return SafePing.safe_ping(host)

# Function to validate and sanitize host input
def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']
    # Add more validation rules as needed
    return host in allowed_hosts