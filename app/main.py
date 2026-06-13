from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error {e}'}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)