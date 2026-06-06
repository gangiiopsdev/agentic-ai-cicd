from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        allowed_hosts = ['localhost', '127.0.0.1']
        if host not in allowed_hosts:
            raise ValueError('Host not allowed')
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not isinstance(host, str) or len(host) == 0:
        raise ValueError('Invalid host parameter')
    return SafePing.safe_ping(host)