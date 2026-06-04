from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

class PingEndpoint:
    @staticmethod
def ping(host: str):
        if not validate_host(host):
            raise ValueError('Invalid host')
        return PingService.safe_ping(host)

    def __init__(self, app: FastAPI):
        self.app = app
        self.app.add_api_route('/ping', self.ping, methods=['GET'])

def validate_host(host: str) -> bool:
    # Add validation logic here
    return True

def setup_ping_endpoint(app: FastAPI):
    PingEndpoint(app)