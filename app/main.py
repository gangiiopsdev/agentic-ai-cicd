from fastapi import FastAPI
import re

class SafePing:
    @staticmethod
def ping(host: str):
        # Regex to validate host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'error': 'Invalid host input'}
        try:
            result = subprocess.run(['ping', host], check=True, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error {e}'}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)