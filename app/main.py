from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def ping(host: str):
        if host == 'localhost' or host.startswith('127.0.0.1') or host.startswith('::1'):
            try:
                result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
                return {'status': 'completed', 'output': result.stdout}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafeCommand.ping(host)