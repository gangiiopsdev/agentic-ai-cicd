from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid hostname')
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a whitelist for allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid hostname')
    return safe_ping(host)