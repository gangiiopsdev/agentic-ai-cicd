from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Define a whitelist of allowed hosts or patterns
    allowed_hosts = ['192.168.1.', 'localhost']
    if any(host.startswith(allowed) for allowed in allowed_hosts):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Unauthorized host'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)