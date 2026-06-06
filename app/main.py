from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def safe_ping(host):
        # Sanitize the input using regex to allow only alphanumeric characters and hyphens, with a maximum length of 50 characters
        if not re.match(r'^[a-zA-Z0-9-]{1,50}$', host):
            return {'status': 'failed', 'error': 'Invalid host name'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = SafePing.safe_ping(host)
    return response