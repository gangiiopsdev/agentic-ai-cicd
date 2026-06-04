from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with whitelisting
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_secure(host: str):
    # Validate input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

# Helper function to validate host input
def is_valid_host(host: str) -> bool:
    # Simple validation, more complex logic can be implemented based on requirements
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)