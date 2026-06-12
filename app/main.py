from fastapi import FastAPI
import subprocess
from pydantic import validator

class SafeSubprocess:
    @staticmethod
    def ping(host: str):
        # Secure implementation using subprocess.run with args parameter
        try:
            subprocess.run(['ping', host], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')
            return False

class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping_endpoint(host: str):
        if not host.isalnum():  # Basic validation for alphanumeric characters only
            return {'status': 'failed', 'reason': 'Invalid input'}
        result = SafeSubprocess.ping(host)
        if result:
            return {'status': 'completed'}
        else:
            return {'status': 'failed'}