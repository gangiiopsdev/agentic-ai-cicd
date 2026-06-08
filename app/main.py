from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid hostname'}
    return SafePing.ping(host)