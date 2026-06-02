from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
            return output.decode().strip()
        except subprocess.CalledProcessError as e:
            return str(e.output).decode().strip()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent command injection
    if not SafePing.is_valid_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = SafePing.safe_ping(host)
    return {'status': 'completed', 'result': result}

class SafePing:
    @staticmethod
def is_valid_host(host):
        import re
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None