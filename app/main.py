from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            output = subprocess.check_output(['ping', f'-c 1 {host}'], stderr=subprocess.STDOUT, timeout=10)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)