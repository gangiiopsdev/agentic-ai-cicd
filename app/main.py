from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 403
    else:
        return {'error': 'Unauthorized access'}, 403

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Unauthorized access'}, 403
    return safe_ping(host)

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts