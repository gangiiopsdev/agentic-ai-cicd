from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate input to prevent command injection
            if not all(c.isalnum() or c in ['.', '-'] for c in host):
                raise ValueError('Invalid hostname')
            subprocess.run(['ping', host], check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = SafePing.safe_ping(host)
    return result