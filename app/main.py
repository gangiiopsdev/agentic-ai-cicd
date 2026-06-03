from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if '@' in host or '&' in host or ';' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Safe implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate the input to ensure it does not contain malicious content
    if '@' in host or '&' in host or ';' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)