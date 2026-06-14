from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.run(['ping', '-c', 4, host], check=True)
        else:
            raise ValueError('Unauthorized host')

app = FastAPI()
ping_service = SafePing()

@app.get('/ping')
def ping(host: str):
    try:
        ping_service.ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}