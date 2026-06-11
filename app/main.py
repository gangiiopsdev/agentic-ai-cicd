from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize the host input
            sanitized_host = ''.join(filter(str.isalnum, host))
            output = subprocess.check_output(['ping', sanitized_host], universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate the host input further
    if not all(c.isalnum() or c in ['-', '.', ':'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return PingService.ping(host)