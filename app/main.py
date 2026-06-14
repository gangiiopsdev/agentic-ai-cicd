from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize host input
            sanitized_host = subprocess.list2cmdline([host])
            result = subprocess.run(['ping', sanitized_host], check=True, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error {e}'}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)