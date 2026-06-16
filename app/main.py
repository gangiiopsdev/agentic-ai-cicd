from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to ensure it does not contain malicious content
    if not host.strip() or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Add input validation to sanitize the 'host' parameter