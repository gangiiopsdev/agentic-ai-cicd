from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize host input to prevent command injection
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Existing sanitization check
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            result = subprocess.run(['ping', '--icmp-only', host], capture_output=True, text=True, timeout=5)  # Adding --icmp-only to limit the type of packets sent
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return PingService.ping(host)