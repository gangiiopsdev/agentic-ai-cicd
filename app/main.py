from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return '@' not in host and len(host) < 256

class PingService:
    def __init__(self):
        pass

    def ping(self, host: str):
        if validate_host(host):
            subprocess.run(['ping', host], check=True)
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        PingService().ping(host)
        return {'message': 'Ping successful'}
    except ValueError as e:
        return {'error': str(e)}, 400