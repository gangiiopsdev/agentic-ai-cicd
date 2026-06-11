from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

def is_valid_host(host):
    # Implement validation logic here (e.g., regex pattern matching)
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)