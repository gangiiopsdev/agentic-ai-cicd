from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host parameter to ensure it only contains allowed characters and format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Use a safe command with parameters to avoid shell=True and potential injection
        result = subprocess.run(['ping', '-c', 4, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional validation and error handling can be added here