from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafePing.safe_ping(host)