from fastapi import FastAPI
import subprocess

class PingCommand:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate host input to prevent command injection
            if not all(c.isalnum() or c in '.-' for c in host):
                raise ValueError('Invalid host name')
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return PingCommand.safe_ping(host)