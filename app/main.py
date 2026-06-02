from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def validate_host(host: str) -> bool:
        try:
            int(host)
            return True
        except ValueError:
            return False

    @staticmethod
def ping(host: str):
        if not SafePing.validate_host(host):
            return {'status': 'error', 'message': 'Invalid input'}
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.post('/ping/')
def ping_endpoint(host: str):
    return SafePing.ping(host)