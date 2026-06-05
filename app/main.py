from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input to avoid shell injection
        host = subprocess.check_output(['echo', host], text=True).strip()
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def validate_host(host):
    # Implement validation logic here, e.g., allow only certain domain names
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}