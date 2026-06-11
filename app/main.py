from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)