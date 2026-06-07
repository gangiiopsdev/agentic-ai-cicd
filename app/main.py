from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if host is an IP address or hostname
    return True

@app.get('/ping')
def ping(host: str):
    try:
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        # Use shlex to safely quote arguments
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}