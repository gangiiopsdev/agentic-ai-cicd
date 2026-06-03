from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the input to prevent command injection
        if not all(c.isalnum() or c in '.-@' for c in host):
            return {'status': 'error', 'output': 'Invalid hostname'}
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return SafePing.ping(host)