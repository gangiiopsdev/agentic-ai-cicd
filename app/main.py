from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host.strip()

app = FastAPI()

@app.post('/ping/')
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input
        if not request.host.isalnum():
            raise ValueError('Invalid host name')
        subprocess.run(['ping', request.host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}