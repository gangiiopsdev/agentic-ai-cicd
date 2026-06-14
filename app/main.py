from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple validation for demonstration purposes
    if not host.isdigit():
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}