from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    service = PingService()
    # Use regex to sanitize the input more rigorously
    import re
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return service.ping(sanitized_host)