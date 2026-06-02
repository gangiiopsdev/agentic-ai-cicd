from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the input to prevent command injection
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    # Example: Only allow alphanumeric characters and hyphens
    return host.isalnum() or '-' in host