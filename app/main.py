from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafePing.ping(host)

# Enhanced validation to sanitize host input further
import re
def validate_host(host: str):
    pattern = r'^[a-zA-Z0-9.:-]{1,255}$'
    if not re.match(pattern, host):
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return SafePing.ping(host)