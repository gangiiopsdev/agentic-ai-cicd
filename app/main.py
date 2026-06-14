from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        allowed_hosts = ['host1', 'host2']  # Define a whitelist of allowed hosts
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Host is not allowed'}
        try:
            result = subprocess.run(['ping', *host.split()], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    if any(char in host for char in [';', '&', '|', '`']):  # Check for potential injection characters
        return {'status': 'failed', 'error': 'Potential command injection detected'}
    return SafeSubprocess.ping(host)