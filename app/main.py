from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a whitelist of allowed hosts for security
        allowed_hosts = ['8.8.8.8', '127.0.0.1']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)