from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '--', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a whitelist and validate the input
    if not host.isdigit() or len(host) != 15:
        return {'status': 'error', 'message': 'Invalid host format'}
    return safe_ping(host)