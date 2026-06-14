from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content.
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Implement a validation function to check for malicious patterns in the host input.
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False