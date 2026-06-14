from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe
    return '.' in host and not any(char.isdigit() for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}