from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

# Helper function to validate the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., whitelist of allowed hosts)
    return True