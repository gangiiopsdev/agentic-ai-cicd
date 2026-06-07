from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a whitelist of allowed hosts or perform additional validation
        if host in ['allowed_host1', 'allowed_host2']:
            sanitized_host = subprocess.list2cmdline([host])
            subprocess.run(['ping', sanitized_host], check=True)
            return {'status': 'completed'}
        else:
            return {'error': 'Host not allowed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)